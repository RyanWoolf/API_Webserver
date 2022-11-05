from config import db


class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String())
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String())
    visited = db.Column(db.Integer, default=0)