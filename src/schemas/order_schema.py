from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError


class OrderSchema(ma.Schema):
    table = fields.Nested('TableSchema', only=['number'])
    staff = fields.Nested('StaffSchema', only=['id', 'staff_name'])
    
    class Meta:
        fields = ('id', 'date', 'table', 'staff', 'total_price', 'is_paid')
        ordered = True