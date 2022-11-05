from config import db


class Order_detail(db.Model):
    __tablename__ = 'order_detail'
    
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)