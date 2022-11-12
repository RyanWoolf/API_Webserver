from flask import Blueprint, request
from config import db, bcrypt, query_by_id, not_found
from models.customer import Customer
from schemas.customer_schema import CustomerSchema
from controllers.auth_controller import authorization, authorization_admin
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token
from datetime import timedelta


customers_bp = Blueprint('customers', __name__, url_prefix='/customers')


#Getting all customers from the db
@customers_bp.route('/')
@jwt_required()
def all_customers():
    authorization()
    stmt = db.select(Customer).order_by(Customer.id)
    customers = db.session.scalars(stmt)
    return CustomerSchema(many=True, exclude=['password']).dump(customers)
    
    
#Get specific customer with id
@customers_bp.route('/<int:id>/')
@jwt_required()
def get_one_customer(id):
    authorization()
    customer = query_by_id(Customer, id)
    if customer:
        return CustomerSchema(exclude=['password']).dump(customer)
    else:
        return not_found('Customer', id)
    
    
#Get specific customer with a first name
@customers_bp.route('/<string:f_name>/')
@jwt_required()
def search_customer(f_name):
    authorization()
    stmt = db.select(Customer).filter_by(first_name=f_name.capitalize())
    customers = db.session.scalars(stmt)
    # We can't guess the result is none or only one or more than one. 
    # So use condition on len(result) to know the result has at lease one 
    result = CustomerSchema(many=True, exclude=['password']).dump(customers)
    if len(result) == 0:
        return {'error': f'Customer {f_name} not found'}, 404
    else:
        return result


#Get specific customer with full name. first name and last name
@customers_bp.route('/<string:f_name>/<string:l_name>/')
@jwt_required()
def search_customer_fullname(f_name, l_name):
    authorization()
    stmt = db.select(Customer).filter_by(
        first_name=f_name.capitalize(), 
        last_name=l_name.capitalize())
    customers = db.session.scalars(stmt) # there could be lots of customers with exactly same name
    result = CustomerSchema(many=True, exclude=['password']).dump(customers)
    if len(result) == 0:
        return {'error': f'Customer {f_name} {l_name} not found'}, 404
    else:
        return result


#New customer join through here
@customers_bp.route('/join/', methods=['POST'])
def customer_join():
    try:
        data = CustomerSchema().load(request.json)
        customer = Customer(
            email = data['email'],
            password = bcrypt.generate_password_hash(data['password']).decode('utf-8'),
            first_name = data['first_name'].capitalize(),
            last_name = data.get('last_name').capitalize(),
            phone = data['phone']
        )
        db.session.add(customer)
        db.session.commit()
        token = create_access_token(identity=str(customer.id), expires_delta=timedelta(days=1))
        return {'msg': f'{customer.email} registered. Welcome {customer.first_name}.', 'token': f'{token}'}, 201
    except IntegrityError:
        return {'error': 'Email is already in use. Please try with a different email address'}, 409


# Customer login through here
@customers_bp.route('/login/')
def customer_login():
    stmt = db.select(Customer).filter_by(email=request.json['email'])
    customer = db.session.scalar(stmt)
    if customer and bcrypt.check_password_hash(customer.password, request.json['password']):
        token = create_access_token(identity=str(customer.id), expires_delta=timedelta(days=1))
        return {'msg': f'Welcome. {customer.first_name} {customer.last_name}', 'token': token}
    else:
        return {'error': 'Invalid email or password'}, 401


#Delete customer from the DB. For safety reasons, only accessible through id
@customers_bp.route('/<int:id>/', methods = ['DELETE'])
@jwt_required()
def delete_one_customer(id):
    authorization_admin()
    customer = query_by_id(Customer, id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return {'msg': f'Customer id: {id} {customer.first_name} {customer.last_name} deleted successfully'}
    else:
        return not_found('Customer', id)


#Modify customer. Only accessible through id
@customers_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_customer(id):
    authorization_admin()
    customer = query_by_id(Customer, id)
    if customer:
        customer.first_name = request.json.get('first_name') or customer.first_name
        customer.last_name = request.json.get('last_name') or customer.last_name
        customer.phone = request.json.get('phone') or customer.phone
        customer.email = request.json.get('email') or customer.email
        customer.visited = request.json.get('visited') or customer.visited
        db.session.commit()
        return CustomerSchema(exclude=['password']).dump(customer)
    else:
        return not_found('Customer', id)