from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError


class Order_FoodSchema(ma.Schema):
    order = fields.Nested('OrderSchema', only=['id'])
    food = fields.Nested('FoodSchema', only=['id'])
    
    class Meta:
        fields = ('id', 'food', 'quantity', 'order')
        ordered = True