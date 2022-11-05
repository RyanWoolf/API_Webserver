from flask import Blueprint
from flask_jwt_extended import jwt_required
from config import db, bcrypt
from datetime import date
from models.staff import Staff
from models.food import Food


db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Initial config created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Initial config dropped")

@db_commands.cli.command('seed')
def seed_db():
    staffs = [
        Staff(
            login_id='admin',
            password=bcrypt.generate_password_hash('lwhaus').decode('utf-8'),
            is_admin=True
        )
    ]
    foods = [
        Food(
            name = 'Steak Sandwich',
            price = 25
        ),
        Food(
            name = 'Fish&Chips',
            price = 24,
            is_df = True
        ),
        Food(
            name = 'Beef Burger',
            price = 26,
            is_df = True
        ),
        Food(
            name = 'Prawn Pasta',
            price = 28
        ),
        Food(
            name = 'Mushroom Risotto',
            price = 23,
            is_v = True
        ),
        Food(
            name = 'Angus Sirloin Steak',
            price = 29,
            is_gf = True
        ),
        Food(
            name = 'Pan fried Barramundi Fillet',
            price = 29,
            is_gf = True,
            is_df = True
        ),
        Food(
            name = 'Southern Fried Chicken Burger',
            price = 25,
            is_gf = True
        ),
        Food(
            name = 'Bowl of Fries',
            price = 12,
            is_gf = True,
            is_v = True
        ),
        Food(
            name = 'Steamed Veges',
            price = 12,
            is_gf = True,
            is_df = True,
            is_v = True
        ),
        Food(
            name = 'Garden salad',
            price = 12,
            is_gf = True,
            is_v = True
        ),
        Food(
            name = 'Affogato',
            price = 12,
            is_gf = True,
            is_v = True
        )
    ]
    db.session.add_all(staffs)
    db.session.add_all(foods)
    db.session.commit()
    
    print('Initial config seeded')