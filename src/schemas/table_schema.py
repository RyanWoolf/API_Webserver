from config import ma
from marshmallow import fields
from marshmallow.validate import Range


class TableSchema(ma.Schema):
    seats = fields.Integer(required=True, validate=Range(2, 8, error='Must be between 2 and 8'))
    
    class Meta:
        fields = ('id', 'number', 'seats')
        ordered = True
        