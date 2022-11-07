from config import db


class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String())
    password = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    visited = db.Column(db.Integer, default=0) # how many times visited
    is_staff = db.Column(db.Boolean, default=False)
    
    bookings = db.relationship('Booking', back_populates="customer")