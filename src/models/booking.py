from config import db


class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    pax = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(150))
    
    # FK area
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'), nullable=False)
    
    # Field for FKs
    customer = db.relationship('Customer', back_populates="bookings")
    table = db.relationship('Table', back_populates="bookings")