from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Range, OneOf, And, Regexp


class TableSchema(ma.Schema):
    
    class Meta:
        fields = ('id', 'number', 'seats')
        ordered = True