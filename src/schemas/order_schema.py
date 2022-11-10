from config import ma
from marshmallow import fields


class OrderSchema(ma.Schema):
    staff = fields.Nested('StaffSchema', only=['id', 'staff_name'])  
    table = fields.Nested('TableSchema', only=['number'])
    food = fields.Nested('Order_FoodSchema', many=True)
    is_paid = fields.Boolean()
     
    class Meta:
        fields = ('id', 'date', 'table', 'staff', 'total_price', 'is_paid', 'food')
        ordered = True
