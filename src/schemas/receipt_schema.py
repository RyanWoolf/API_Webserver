from config import ma, db
from marshmallow import fields


class ReceiptSchema(ma.Schema):
    payments = fields.Nested('PaymentSchema', only=['method'])
    orders = fields.Nested('OrderSchema', only=['id', 'total_price'])
    
    class Meta:
        fields = ('id', 'payments', 'orders')
        ordered = True