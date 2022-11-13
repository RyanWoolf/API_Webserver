from flask import Blueprint, request
from config import db, query_by_id, not_found
from models.payment import Payment
from schemas.payment_schema import PaymentSchema, VALID_PAYMENT
from controllers.auth_controller import authorization_admin, authorization
from flask_jwt_extended import jwt_required


payments_bp = Blueprint('payments', __name__, url_prefix='/payments')


#Getting all methods from the db
@payments_bp.route('/')
@jwt_required()
def all_methods():
    authorization()
    stmt = db.select(Payment).order_by(Payment.id)
    foods = db.session.scalars(stmt)
    return PaymentSchema(many=True).dump(foods), 201
    
 
#Add new method in the DB, only admin is allowed to do this
@payments_bp.route('/', methods=['POST'])
@jwt_required()
def add_method():
    authorization_admin()
    new_method = request.json['method']
    if not isinstance(new_method, str):
        return {'error': 'It must be a string'}
    method = Payment(
        method = new_method.capitalize()
    )
    db.session.add(method)
    db.session.commit()
    VALID_PAYMENT.append(method.method)
    return PaymentSchema().dump(method), 201


#Delete method from the DB. For safety reasons, only accessible through id
@payments_bp.route('/<int:id>/', methods = ['DELETE'])
@jwt_required()
def delete_one_method(id):
    authorization_admin()
    method = query_by_id(Payment, id)
    if method:
        VALID_PAYMENT.remove(method.method)
        db.session.delete(method)
        db.session.commit()
        return {'msg': f'Payment method: {method.method} deleted successfully'}
    else:
        return not_found('Payment', id)


#Modify food. Only accessible through id
@payments_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_method(id):
    authorization_admin()
    method = query_by_id(Payment, id)
    new_method = request.json['method']
    if not isinstance(new_method, str):
        return {'error': 'It must be a string'}
    if method:
        VALID_PAYMENT.remove(method.method)
        method.method = new_method
        VALID_PAYMENT.append(new_method)
        db.session.commit()
        return PaymentSchema().dump(method)
    else:
        return not_found('Payment', id)