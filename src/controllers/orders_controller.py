from flask import Blueprint, request
from config import db, query_by_id, not_found, not_found_simple
from models.order import Order
from models.food import Food
from models.staff import Staff
from models.table import Table
from models.order_food import Order_Food
from schemas.order_schema import OrderSchema
from schemas.table_schema import TableSchema  # Needs for modify order endpoint
from controllers.auth_controller import authorization_admin, authorization
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date


orders_bp = Blueprint('orders', __name__, url_prefix='/orders')


# Total tables counts for future new table added in the db
def total_tables():
    stmt2 = db.select(db.func.count()).select_from(Table)
    max_table = db.session.scalar(stmt2)
    return max_table


#Getting all orders from the db
@orders_bp.route('/')
@jwt_required()
def all_orders():
    authorization()
    stmt = db.select(Order).order_by(Order.id)
    orders = db.session.scalars(stmt)
    return OrderSchema(many=True).dump(orders)
    
    
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
@orders_bp.route('/<string:year>/<string:month>/<string:day>')
@jwt_required()
def search_orders_date(year, month, day):
    authorization()
    date_to_search = '-'.join([year, month, day])
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
    stmt = db.select(Order).filter_by(id=id)
    order = db.session.scalar(stmt)
    if order:
        db.session.delete(order)
        db.session.commit()
        return {'msg': f'Order id: {id} deleted successfully'}
    else:
        return not_found('Order', id)
    

#Modify order. Only accessible through id
@orders_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_order(id):
    authorization_admin()
    order = query_by_id(Order, id)
    total_table = total_tables()
    if order:
        order.total_price = request.json.get('total_price') or order.total_price # for example, discount reason
        order.is_paid = request.json.get('is_paid') if request.json.get('is_paid') is not None else order.is_paid
        staff = request.json.get('staff')
        table = request.json.get('table')
        if staff:
            staff_new = query_by_id(Staff, staff)
            if not staff_new:
                return not_found_simple('Staff')
            order.staff = staff_new
        if table:
            if int(table) > total_table:
                return not_found_simple('Table')
            table_new = query_by_id(Table, table)
            order.table = table_new
        food = request.json.get('food')
        if food:
            stmt = db.select(Order_Food).filter_by(order_id=id, food_id=food)
            food_current = db.session.scalar(stmt)
            if food_current:
                qty_new = request.json.get('quantity')
                food_new = query_by_id(Food, food)
                qty_before = food_current.quantity
                db.session.query(Order_Food).filter(
                    Order_Food.order_id == id, 
                    Order_Food.food_id == food).update(
                        {"quantity": qty_new}, synchronize_session="fetch")
                order.total_price += food_new.price * (qty_new - qty_before)
            else:
                return {'error': 'Food not found in the order'}, 404
        db.session.commit()
        return OrderSchema().dump(order)
    else:
        return not_found('Order', id)
    

# Place a new order
@orders_bp.route('/new/table<int:table_number>', methods=['POST'])
@jwt_required()
def create_order(table_number):
    authorization()
    open_table = query_by_id(Table, table_number)
    staff_id = query_by_id(Staff, get_jwt_identity())
    order = Order(
        staff = staff_id,
        table = open_table,
        date = date.today())
    db.session.add(order)
    db.session.commit()
    data = request.json
    total_json_keys, n = len(data.keys()), 1
    foods_list = []
    while n <= total_json_keys // 2:
        food_id = request.json[f'food_{n}']
        food_db = query_by_id(Food, food_id)
        if not food_db:
            return {'error': f'food id {food_id} not found'}, 404
        food = (food_db, request.json[f'quantity_{n}'])
        foods_list.append(food)
        n += 1
    order.generate_order_food(foods_list)
    order.calc_total_price(foods_list)
    db.session.commit()
    return {'msg': f'Order id:{order.id} has been through successfully'}, 201
# Hopefully payment system can be built before last commit


# Check the todays order from a table
@orders_bp.route('/open/table<int:table_number>', methods=['POST'])
@jwt_required()
def check_order_table(table_number):
    authorization()
    stmt = db.select(Order).filter_by(table_id=table_number, date=date.today())
    table = db.session.scalars(stmt)
    result = OrderSchema(many=True).dump(table)
    if len(result) == 0:
        return {'error': f'Order in table {table_number} not found.'}, 404
    else:
        return result