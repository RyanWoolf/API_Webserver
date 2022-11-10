from config import ma


class StaffSchema(ma.Schema):
    
    class Meta:
        fields = ('id', 'staff_name', 'login_id', 'password', 'is_admin')
        ordered = True