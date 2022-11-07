from flask import Blueprint, request, url_for, redirect
from config import db
from models.customer import Customer
from schemas.customer_schema import CustomerSchema
from controllers.auth_controller import authorization, authorization_admin
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required


customers_bp = Blueprint('customers', __name__, url_prefix='/customers')


def not_found(id):
    return {'error': f'Customer {id} not found.'}, 404


#Getting all customers from the db
@customers_bp.route('/')
@jwt_required()
def all_customers():
    authorization()
    stmt = db.select(Customer).order_by(Customer.id)
    customers = db.session.scalars(stmt)
    return CustomerSchema(many=True).dump(customers), 201
    
    
#Get specific customer with id
@customers_bp.route('/<int:id>/')
@jwt_required()
def get_one_customer(id):
    authorization()
    stmt = db.select(Customer).filter_by(id=id)
    customer = db.session.scalar(stmt)
    if customer:
        return CustomerSchema().dump(customer)
    else:
        return not_found(id)
    
    
#Get specific customer with a first name
@customers_bp.route('/<string:f_name>/')
@jwt_required()
def search_customer(f_name):
    authorization()
    stmt = db.select(Customer).filter_by(first_name=f_name.capitalize())
    customer = db.session.scalars(stmt)
    # We can't guess the result is none or only one or more than one. 
    # So use condition on len(result) to distinguish how many result could be returned
    result = CustomerSchema(many=True).dump(customer)
    if len(result) == 0:
        return {'error': f'Customer {f_name} not found'}, 404
    else:
        return result


#Get specific customer with full name. first name/last name
@customers_bp.route('/<string:f_name>/<string:l_name>')
@jwt_required()
def search_customer_fullname(f_name, l_name):
    authorization()
    stmt = db.select(Customer).filter_by(
        first_name=f_name.capitalize(), 
        last_name=l_name.capitalize())
    customer = db.session.scalars(stmt) # there could be lots of customers with exactly same name
    result = CustomerSchema(many=True).dump(customer)
    if len(result) == 0:
        return {'error': f'Customer {f_name} {l_name} not found'}, 404
    else:
        return result



#Add new customer in the DB, only admin is allowed to do this
@customers_bp.route('/', methods=['POST'])
@jwt_required()
def add_customer():
    authorization_admin()
    data = CustomerSchema().load(request.json)
    customer = Customer(
        first_name = data['first_name'].capitalize(),
        last_name = data.get('last_name').capitalize(),
        phone = data['phone'],
        email = data.get('email')
    )
    db.session.add(customer)
    db.session.commit()
    return CustomerSchema().dump(customer), 201


#Delete customer from the DB. For safety reasons, only accessible through id
@customers_bp.route('/<int:id>/', methods = ['DELETE'])
@jwt_required()
def delete_one_customer(id):
    authorization_admin()
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
@jwt_required()
def update_one_customer(id):
    authorization_admin()
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