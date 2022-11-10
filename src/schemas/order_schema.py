from config import ma
from marshmallow import fields, validates
from marshmallow.validate import Range
from marshmallow.exceptions import ValidationError


class OrderSchema(ma.Schema):
    # table = fields.Integer(required=True, valildate=(Range(1,20, error='Table does not exist. Please try again.')))
    staff = fields.Nested('StaffSchema', only=['id', 'staff_name'])  
    table = fields.Nested('TableSchema', only=['id'])
     
    class Meta:
        fields = ('id', 'date', 'table', 'staff', 'total_price', 'is_paid')
        ordered = True


# class OrderSchema(ma.Schema):
#     # table = fields.Nested('TableSchema', only=['number'])
#     table = fields.Integer(required=True, valildate=(Range(1,20, error='Table does not exist. Please try again.')))
#     staff = fields.Nested('StaffSchema', only=['id', 'staff_name'])
    
#     class Meta:
#         fields = ('id', 'date', 'table', 'staff', 'total_price', 'is_paid')
#         ordered = True