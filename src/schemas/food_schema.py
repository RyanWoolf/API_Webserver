from config import ma, db
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError


class FoodSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price', 'is_gf', 'is_df', 'is_v')
        ordered = True