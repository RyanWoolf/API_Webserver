from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Range, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError


class BookingSchema(ma.Schema):
    customer = fields.Nested('CustomerSchema', exclude=['id', 'password'])
    table = fields.Nested('TableSchema', exclude=['id'])
    
    pax = fields.Integer(validate=(
        Range(1,8, error='It\'s over max 8 pax. Please contact the manager for group booking')))
    date = fields.Date()
    time = fields.Time('%H:%M')
    
    class Meta:
        fields = ('id', 'date', 'time', 'pax', 'comment', 'customer', 'table')
        ordered = True