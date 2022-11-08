from config import db
from sqlalchemy.orm import backref, relationship

class Food(db.Model):
    __tablename__ = 'foods'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    is_gf = db.Column(db.Boolean, default=False)
    is_df = db.Column(db.Boolean, default=False)
    is_v = db.Column(db.Boolean, default=False)
    
    orders = relationship('Order', secondary='order_food', viewonly=True)
    # order_detail = db.relationship('Order_detail', back_populates='food')
    
