from config import db


class Table(db.Model):
    __tablename__ = 'tables'
    
    # mostly we'll use number to find a table instead of id
    # because in some cases, table can be arranged like 1-5 then 10-15. it means id and number can't be matched
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    seats = db.Column(db.Integer, nullable=False)
    
    # Fields for FK
    bookings = db.relationship('Booking', back_populates="table")
    orders = db.relationship('Order', back_populates='table')