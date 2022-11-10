from config import ma
from marshmallow import fields


class FoodSchema(ma.Schema):
    name = fields.String()
    price = fields.Integer()
    is_gf = fields.Boolean()
    is_df = fields.Boolean()
    is_v = fields.Boolean()
    
    
    class Meta:
        fields = ('id', 'name', 'price', 'is_gf', 'is_df', 'is_v')
        ordered = True