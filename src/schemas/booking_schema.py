from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Range, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError


class BookingSchema(ma.Schema):
    customer = fields.Nested('CustomerSchema', exclude=['id', 'password'])
    table = fields.Nested('TableSchema', exclude=['id'])
    pax = fields.Integer(required=True, 
                        validate=(Range(1,8, error='It\'s over Max 8 pax. Please contact the manager for group booking')))
    
    class Meta:
        fields = ('id', 'date', 'time', 'pax', 'comment', 'customer', 'table')
        ordered = True