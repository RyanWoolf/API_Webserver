from config import db


class Customer(db.Model):
    __tablename__ = 'customers'
    
    # Customers id is starting from 100. This is to distinguish between Customer and Staff for using token
    # Because otherwise, the id number in TOKEN could be the same from one of the staffs id
    id = db.Column(db.Integer, db.schema.Identity(start=100), primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String())
    password = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    visited = db.Column(db.Integer, default=0) # how many times visited counts
    
    # Field for FKs
    bookings = db.relationship('Booking', back_populates="customer")