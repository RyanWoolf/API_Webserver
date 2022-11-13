from flask import Blueprint, request
from config import db, query_by_id, not_found, not_found_simple
from models.receipt import Receipt
from models.order import Order
from models.payment import Payment
from schemas.receipt_schema import ReceiptSchema
from schemas.payment_schema import PaymentSchema
from controllers.auth_controller import authorization_admin, authorization
from flask_jwt_extended import jwt_required


receipts_bp = Blueprint('receipts', __name__, url_prefix='/receipts')


# Get all receipt
@receipts_bp.route('/')
@jwt_required()
def all_receipts():
    authorization()
    stmt = db.select(Receipt).order_by(Receipt.id)
    receipts = db.session.scalars(stmt)
    return ReceiptSchema(many=True).dump(receipts)


#Get specific receipt with id
@receipts_bp.route('/<int:id>/')
@jwt_required()
def get_one_receipt(id):
    authorization()
    receipt = query_by_id(Receipt, id)
    if receipt:
        return ReceiptSchema().dump(receipt)
    else:
        return not_found_simple('Receipt')
    
    
#Delete receipt from the DB. For safety reasons, only accessible through id
@receipts_bp.route('/<int:id>/', methods = ['DELETE'])
@jwt_required()
def delete_one_receipt(id):
    authorization_admin()
    receipt = query_by_id(Receipt, id)
    if receipt:
        db.session.delete(receipt)
        db.session.commit()
        return {'msg': f'Receipt id: {id} deleted successfully'}
    else:
        return not_found('Order', id)


## Create new receipt
@receipts_bp.route('/table<int:number>/', methods = ['POST'])
@jwt_required()
def create_receipt(number):
    authorization()
    stmt = db.select(Order).filter_by(table_id=number, is_paid=False)   # If is_paid is True, the receipt for this is already processed
    order = db.session.scalar(stmt)
    data_payment = PaymentSchema().load(request.json)
    payment_method = data_payment['method']
    stmt2 = db.select(Payment).filter_by(method=payment_method)
    payment_id = db.session.scalar(stmt2)
    if order:
        new_receipt = Receipt(
            order_id = order.id,
            payment_id = payment_id.id
        )
        db.session.add(new_receipt)
        order.is_paid = True                  # Turning it to True means, now this Order is paid and no need to process again
        db.session.commit()
        return ReceiptSchema().dump(new_receipt), 201
    else:
        return {'error': f'Table {number} is not found'}, 404
    
    
# Modify payment method in receipt
@receipts_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def modify_receipt(id):
    authorization_admin()
    receipt = query_by_id(Receipt, id)
    if receipt:
        data = PaymentSchema().load(request.json)
        new_payment = data['method'].capitalize()
        stmt = db.select(Payment).filter_by(method=new_payment)
        payment_id = db.session.scalar(stmt)
        receipt.payment_id = payment_id.id
        db.session.commit()
        return ReceiptSchema().dump(receipt)
    else:
        return {'error': f'Receipt ID {id} is not found'}, 404