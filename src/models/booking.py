from config import db


class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Datetime, nullable=False)
    pax = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(150))