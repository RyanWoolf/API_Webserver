from config import ma
from marshmallow import fields, validates
from marshmallow.validate import Length, Range, And, Regexp, Email
from marshmallow.exceptions import ValidationError


class CustomerSchema(ma.Schema):
    phone = fields.String(
        validate=And(Length(equal=10, error="Must be 10 digits of numbers"), 
                     Regexp('^[0-9 ]+$', error="Only numbers valid")))
    
    email = fields.String(
        validate=Email(error="Must be valid email address"))
    
    password = fields.String()
    
    first_name = fields.String()
    last_name = fields.String()

    class Meta:
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone', 'visited')
        ordered = True
        