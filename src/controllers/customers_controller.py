from flask import Blueprint, request, url_for, redirect
from config import db
from models.customer import Customer
from schemas.customer_schema import CustomerSchema
from controllers.auth_controller import authorization
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required


customers_bp = Blueprint('customers', __name__, url_prefix='/customers')


def not_found(id):
    return {'error': f'Customer id: {id} not found.'}, 404


#Getting all customers from the db
@customers_bp.route('/')
def all_customers():
    stmt = db.select(Customer).order_by(Customer.id)
    customers = db.session.scalars(stmt)
    return CustomerSchema(many=True).dump(customers), 201
    
    
#Get specific customer with id
@customers_bp.route('/<int:id>/')
def get_one_customer(id):
    stmt = db.select(Customer).filter_by(id=id)
    customer = db.session.scalar(stmt)
    if customer:
        return CustomerSchema().dump(customer)
    else:
        return not_found(id)
    
    
#Get specific customer with a first name
@customers_bp.route('/<string:tag>/')
def search_food(tag):
    if not tag.lower() in tags:
        return {'error': 'Failed to search. Please check the tag and try again.'}, 404
    else:
        if tag.lower() == 'gf':
            stmt = db.select(Food).filter_by(is_gf=True)
            food = db.session.scalars(stmt)
        elif tag.lower() == 'df':
            stmt = db.select(Food).filter_by(is_df=True)
            food = db.session.scalars(stmt)
        elif tag.lower() == 'v':
            stmt = db.select(Food).filter_by(is_v=True)
            food = db.session.scalars(stmt)
        return CustomerSchema(many=True, only=['name', 'price']).dump(food)


#Get specific foods with two tags(GF, DF, V)
@customers_bp.route('/<string:tag1>/<string:tag2>')
def search_food_tags(tag1, tag2):
    tag1, tag2 = tag1.lower(), tag2.lower()
    if tag1 not in tags or tag2 not in tags:
        return {'error': 'Failed to search. Please check the tag and try again.'}, 404
    elif tag1 == tag2: # If you put two same tags, it redirects to search_food
        return redirect(url_for('foods.search_food', tag = tag1))
    rest = list(tags)
    rest.remove(tag1)
    rest.remove(tag2)
    if 'v' in rest:
        stmt = db.select(Food).filter_by(is_gf=True, is_df=True)
        food = db.session.scalars(stmt)
    elif 'gf' in rest:
        stmt = db.select(Food).filter_by(is_df=True, is_v=True)
        food = db.session.scalars(stmt)
    elif 'df' in rest:
        stmt = db.select(Food).filter_by(is_v=True, is_gf=True)
        food = db.session.scalars(stmt)
    return CustomerSchema(many=True, only=['name', 'price']).dump(food)



#Add new food in the DB, only admin is allowed to do this
@customers_bp.route('/', methods=['POST'])
# @jwt_required()
def add_food():
    # authorization()
    data = CustomerSchema().load(request.json)
    food = Food(
        name = data['name'],
        price = data['price'],
        is_gf = data.get('is_gf'),
        is_df = data.get('is_df'),
        is_v = data.get('is_v'),
    )
    db.session.add(food)
    db.session.commit()
    return CustomerSchema().dump(food), 201


#Delete customer from the DB. For safety reasons, only accessible through id
@customers_bp.route('/<int:id>/', methods = ['DELETE'])
# @jwt_required()
def delete_one_customer(id):
    # authorization()
    stmt = db.select(Customer).filter_by(id=id)
    customer = db.session.scalar(stmt)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return {'msg': f'Customer id:{id} {customer.first_name} {customer.last_name} deleted successfully'}
    else:
        return not_found(id)


#Modify customer. Only accessible through id
@customers_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
# @jwt_required()
def update_one_customer(id):
    # authorization()
    stmt = db.select(Customer).filter_by(id=id)
    customer = db.session.scalar(stmt)
    if customer:
        customer.first_name = request.json.get('first_name') or customer.first_name
        customer.last_name = request.json.get('last_name') or customer.last_name
        customer.phone = request.json.get('phone') or customer.phone
        customer.email = request.json.get('email') or customer.email
        customer.visited = request.json.get('visited') or customer.visited
        db.session.commit()
        return CustomerSchema().dump(customer)
    else:
        return not_found(id)