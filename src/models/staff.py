from config import db


class Staff(db.Model):
    __tablename__ = 'staffs'
    
    id = db.Column(db.Integer, primary_key=True)
    staff_name = db.Column(db.String())
    login_id = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    is_staff = db.Column(db.Boolean(), default=True)
    is_admin = db.Column(db.Boolean(), default=False)