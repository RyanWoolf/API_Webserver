from itertools import count
from config import db
from sqlalchemy.orm import backref, relationship
import uuid


class Order_Food(db.Model):
    __tablename__ = 'order_food'
    
    id = db.Column(db.String(35), primary_key=True, unique=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    
    
    order = relationship('Order', backref=backref('order_food', cascade="all, delete-orphan"))
    food = relationship('Food', backref=backref('order_food', cascade="all, delete-orphan"))
    
    
    def __init__(self, order=None, food=None, quantity=None):
        self.id = uuid.uuid4().hex
        self.order = order
        self.food = food
        self.quantity = quantity
    