from config import ma
from marshmallow import fields, validates
from marshmallow.validate import Range, NoneOf, And, Regexp
from sqlalchemy.exc import IntegrityError


class TableSchema(ma.Schema):
    seats = fields.Integer(required=True, validate=Range(2, 8, error='Must be between 2 and 8'))
    
    class Meta:
        fields = ('id', 'number', 'seats')
        ordered = True
        