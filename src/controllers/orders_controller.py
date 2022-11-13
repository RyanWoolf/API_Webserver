from flask import Blueprint, request, jsonify
from config import db, query_by_id, not_found, not_found_simple
from models.order import Order
from models.food import Food
from models.staff import Staff
from models.table import Table
from models.order_food import Order_Food
from schemas.order_food_schema import Order_FoodSchema
from schemas.order_schema import OrderSchema
from schemas.table_schema import TableSchema  # Needs for modify order endpoint
from controllers.auth_controller import authorization_admin, authorization
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import joinedload
from datetime import date
from sqlalchemy.exc import DataError


orders_bp = Blueprint('orders', __name__, url_prefix='/orders')


#Getting all orders from the db
@orders_bp.route('/')
@jwt_required()
def all_orders():
    authorization()
    stmt = db.select(Order).order_by(Order.id)
    orders = db.session.scalars(stmt)
    return OrderSchema(many=True).dump(orders), 201


    
#Get an order with id
@orders_bp.route('/<int:id>/')
@jwt_required()
def open_one_order(id):
    authorization()
    order = query_by_id(Order, id)
    if order:
        return OrderSchema().dump(order)
    else:
        return not_found('Order', id)
    
    
#Get orders of today
@orders_bp.route('/today/')
@jwt_required()
def open_today_orders():
    authorization()
    stmt = db.select(Order).filter_by(date=date.today())
    order = db.session.scalars(stmt)
    result = OrderSchema(many=True).dump(order) # result can be none or one or a lot
    if len(result) == 0:
        return not_found_simple('Orders')
    else:
        return result
    
    
#Search orders by date
@orders_bp.route('/<string:year>/<string:month>/<string:day>/')
@jwt_required()
def search_orders_date(year, month, day):
    authorization()
    date_to_search = '-'.join([year, month, day]) # reform to Datetype format
    stmt = db.select(Order).filter_by(date=date_to_search)
    order = db.session.scalars(stmt)
    result = OrderSchema(many=True).dump(order) # result can be none or one or a lot
    if len(result) == 0:
        return not_found_simple('Orders')
    else:
        return result
    

#Delete order from the DB. For safety reasons, only accessible through id
@orders_bp.route('/<int:id>/', methods = ['DELETE'])
@jwt_required()
def delete_one_order(id):
    authorization_admin()
    order = query_by_id(Order, id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return {'msg': f'Order id: {id} deleted successfully'}
    else:
        return not_found('Order', id)
    

# Check the todays order from a table
@orders_bp.route('/today/table<int:table_number>/')
@jwt_required()
def check_order_table(table_number):
    authorization() 
    stmt = db.select(Order).filter_by(table_id=table_number, date=date.today(), is_paid=False)
    # Find the table using URI, and search for it. If it's paid, No need to be found
    order = db.session.scalars(stmt)
    result = OrderSchema(many=True).dump(order)
    # Because result can be none or one or a lot.
    if len(result) == 0:
        return {'error': f'Order in table {table_number} not found.'}, 404
    else:
        return result

    

# Place a new order
## Very much important part
@orders_bp.route('/new/table<int:table_number>/', methods=['POST'])
@jwt_required()
def create_order(table_number):
    try:
        authorization() ## In order table, Staff id and table id is FKs. It can't be simply taken from integer result
        stmt_table = db.select(Table).filter_by(number=table_number) # search the table by number not ID, reasons is explain in model
        open_table = db.session.scalar(stmt_table) # Take the Table infos
        staff_id = query_by_id(Staff, get_jwt_identity()) # Take the staff id 
        order = Order(
            staff = staff_id,
            table = open_table,
            date = date.today())
        db.session.add(order)
        db.session.commit()
        data = request.json
        total_json_keys, n = len(data.keys()), 1  # We don't want to take one kind of food at one time 
        foods_list = []                           # Using iteration, take as many as you want to put through
        while n <= total_json_keys // 2:          # store the json(in dict form) to a list and count how many foods is there
            food_id = data[f'food_{n}']           # Food and quantity is one set, so half of the entire dict is the total number of food we're trying to order
            if not isinstance(food_id, int):
                return {'error': 'Food id must be integer'}, 400
            food_db = query_by_id(Food, food_id)
            if not food_db:
                return {'error': f'food id {food_id} not found'}, 404
            food = (food_db, data[f'quantity_{n}'])
            if not isinstance(data[f'quantity_{n}'], int):
                return {'error': 'Quantity must be integer'}, 400            
            foods_list.append(food)
            n += 1
        order.generate_order_food(foods_list)     # use class function to generate an instance of Order_Food table 
        order.calc_total_price(foods_list)        # Calculate the total price and update it to Order instance
        db.session.commit()
        return OrderSchema().dump(order), 201
    except DataError:
        return {'error': 'Please check the correct data type'}, 401



#Modify order. Only accessible through id
@orders_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_order(id):
    authorization_admin()
    order = query_by_id(Order, id)
    if order:
        order.total_price = request.json.get('total_price') or order.total_price # this is used for discount reason
        order.is_paid = request.json.get('is_paid') if request.json.get('is_paid') is not None else order.is_paid
        staff = request.json.get('staff')
        table = request.json.get('table')
        if staff:
            if not isinstance(staff, int):  # Check the input is int
                return {'error': 'Staff id must be integer'}, 400
            staff_new = query_by_id(Staff, staff)                       # if yes, search the staff we want
            if not staff_new:                                           # also check the staff we're searching exists
                return not_found_simple('Staff')
            order.staff = staff_new                                     # If all good, set the staff in Order instance
        if table:
            if not isinstance(table, int):  # Check the input is int
                return {'error': 'Table number must be integer'}, 400
            stmt_table = db.select(Table).filter_by(number=table)
            table_new = db.session.scalar(stmt_table)
            order.table_id = table_new.id                               # Same procedure 
        food = request.json.get('food')                                 # Checking the staff and searching the right table is done here
        if food:
            if not isinstance(food, int):   # Check the input is int
                return {'error': 'Food id must be integer'}, 400
            stmt = db.select(Order_Food).filter_by(order_id=id, food_id=food)       # search the detail(Order_Food) using order_id and food_id
            food_current = db.session.scalar(stmt)                                  
            if food_current:
                qty_new = request.json.get('quantity')                              
                if not isinstance(qty_new, int):
                    return {'error': 'Quantity number must be integer'}, 400
                food_new = query_by_id(Food, food)
                qty_before = food_current.quantity
                db.session.query(Order_Food).filter(                                # Update the quantity of the food
                    Order_Food.order_id == id, 
                    Order_Food.food_id == food).update(
                        {"quantity": qty_new}, synchronize_session="fetch")
                order.total_price += food_new.price * (qty_new - qty_before)        # Update the total price
            else:
                return {'error': 'Food not found in the order'}, 404
        db.session.commit()
        return OrderSchema().dump(order)
    else:
        return not_found('Order', id)
    
    