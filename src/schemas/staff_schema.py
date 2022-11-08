from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError


class StaffSchema(ma.Schema):
    orders = fields.Nested('OrderSchema', only=['id'])
    
    class Meta:
        fields = ('id', 'staff_name', 'login_id', 'password', 'is_admin', 'orders')
        ordered = True