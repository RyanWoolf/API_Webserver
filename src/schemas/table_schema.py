from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Range, OneOf, And, Regexp


class TableSchema(ma.Schema):
    bookings = fields.Nested('BookingSchema', only=['id', 'customer'])
    orders = fields.Nested('OrderSchema', only=['id'])
    
    class Meta:
        fields = ('id', 'number', 'seats', 'bookings', 'orders')
        ordered = True