from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError


class TableSchema(ma.Schema):
    class Meta:
        fields = ('id')
        ordered = True