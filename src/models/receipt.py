from config import db


class Receipt(db.Model):
    __tablename__ = 'receipts'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # FK area in the DB
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    payment_id = db.Column(db.Integer, db.ForeignKey('payments.id'))
    
    # Fields for FKs
    orders = db.relationship('Order', back_populates='receipt')
    payments = db.relationship('Payment', back_populates='receipt')
 