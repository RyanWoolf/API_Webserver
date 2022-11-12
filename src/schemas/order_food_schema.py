from config import ma
from marshmallow import fields


class Order_FoodSchema(ma.Schema):
    order = fields.Nested('OrderSchema', only=['id'])
    food = fields.Nested('FoodSchema', only=['id', 'name'])

    
    class Meta:
        fields = ('id', 'food', 'quantity', 'order')
        ordered = True