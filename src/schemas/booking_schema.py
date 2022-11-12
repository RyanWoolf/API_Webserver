from config import ma
from marshmallow import fields
from marshmallow.validate import Range, Length


class BookingSchema(ma.Schema):
    customer = fields.Nested('CustomerSchema', exclude=['id', 'password'])
    table = fields.Nested('TableSchema', exclude=['id'])
    
    pax = fields.Integer(validate=(
        Range(1,8, error='It\'s over max 8 pax. Please contact the manager for group booking')))
    date = fields.Date()
    time = fields.Time('%H:%M')
    customer_id = fields.Integer()
    comment = fields.String(validate=(
        Length(max=150, error='Comment must be less than 150 letters')))
    
    class Meta:
        fields = ('id', 'date', 'time', 'pax', 'comment', 'customer_id', 'customer', 'table')
        ordered = True