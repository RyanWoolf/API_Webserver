from config import ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, Email


class CustomerSchema(ma.Schema):
    phone = fields.String(
        validate=And(Length(equal=10, error="Must be 10 digits of numbers"), 
                     Regexp('^[0-9 ]+$', error="Only numbers valid")))
    # Only for proper phone number format
    
    email = fields.String(
        validate=Email(error="Must be an email address"))
    # only email format valid
    
    password = fields.String()
    first_name = fields.String()
    last_name = fields.String()

    class Meta:
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone', 'visited')
        ordered = True
        