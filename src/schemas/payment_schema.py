from config import ma, db
from marshmallow import fields
from marshmallow.validate import OneOf


VALID_PAYMENT = ['Card', 'Cash', 'Prepaid']
# This can be added via endpoint manually


class myString(fields.String):
    default_error_messages={"invalid": "It must be a string.", "invalid_utf8": "Not a valid utf-8 string."}
# customizing error message. Not much needed

class PaymentSchema(ma.Schema):
    method = myString(validate=OneOf(VALID_PAYMENT, error=f'It must be one of {VALID_PAYMENT}.'))
    
    class Meta:
        fields = ('id', 'method')
        ordered = True