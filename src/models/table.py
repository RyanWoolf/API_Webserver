from config import db


class Table(db.Model):
    __tablename__ = 'tables'
    
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    
    bookings = db.relationship('Booking', back_populates="table")