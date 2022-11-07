from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError


class BookingSchema(ma.Schema):
    customer = fields.Nested('CustomerSchema', exclude=['id', 'password', 'is_staff'])
    
    class Meta:
        fields = ('id', 'date', 'time', 'pax', 'comment', 'customer')
        ordered = True