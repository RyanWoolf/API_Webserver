from config import ma
from marshmallow import fields
from marshmallow.validate import Range


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