from config import ma
from marshmallow import fields

class StaffSchema(ma.Schema):
    staff_name = fields.String()
    login_id = fields.String()
    password = fields.String()
    
    class Meta:
        fields = ('id', 'staff_name', 'login_id', 'password', 'is_admin')
        ordered = True