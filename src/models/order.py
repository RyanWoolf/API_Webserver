from config import db
from models.order_food import Order_Food
from models.food import Food
from sqlalchemy.orm import backref, relationship

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Integer, default=0)
    date = db.Column(db.Date, nullable=False)
    is_paid = db.Column(db.Boolean, default=False)
    
    staff_id = db.Column(db.Integer, db.ForeignKey('staffs.id'), nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'), nullable=False)
    
    staff = db.relationship('Staff', back_populates='orders')
    table = db.relationship('Table', back_populates='orders')
    
    food = relationship('Food', secondary='order_food', viewonly=True)
    
    def generate_order_food(self, items):
        for food, qty in items:
            self.order_food.append(Order_Food(order=self, food=food, quantity=qty))
            
    def calc_total_price(self, items):
        for food, qty in items:
            self.total_price += food.price * qty
    