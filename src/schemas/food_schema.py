from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError


class FoodSchema(ma.Schema):
    name = fields.String()
    price = fields.Integer()
    is_gf = fields.Boolean()
    is_df = fields.Boolean()
    is_v = fields.Boolean()
    
    
    class Meta:
        fields = ('id', 'name', 'price', 'is_gf', 'is_df', 'is_v')
        ordered = True