from config import ma
from marshmallow import fields


class OrderSchema(ma.Schema):
    staff = fields.Nested('StaffSchema', only=['id', 'staff_name'])  
    table = fields.Nested('TableSchema', only=['number'])
    is_paid = fields.Boolean()
    order_id = fields.Nested('Order_FoodSchema', many=True, only=['food', 'quantity'])
     
    class Meta:
        fields = ('id', 'date', 'table', 'staff', 'order_id', 'total_price', 'is_paid')
        ordered = True
