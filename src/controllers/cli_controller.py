from flask import Blueprint
from config import db, bcrypt
from datetime import date
from models.staff import Staff
from models.food import Food
from models.customer import Customer
from models.payment import Payment
from models.table import Table
from models.booking import Booking
from models.payment import Payment
from models.order import Order
from models.receipt import Receipt
from models.order_food import Order_Food ## Need this for seeding
from datetime import date


db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Initial tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Initial tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    # Admin account setup
    staffs = [
        Staff(
            login_id = 'admin',
            password = bcrypt.generate_password_hash('lwhaus').decode('utf-8'),
            is_admin = True
        )
    ]
    db.session.add_all(staffs)
    db.session.commit()    
    
    # Payment methods setup
    payments = [
        Payment(
            method = 'Cash'
        ),
        Payment(
            method = 'Card'
        ),
        Payment(
            method = 'Prepaid'
        )
    ]
    db.session.add_all(payments)
    db.session.commit()
    
    # Initial tables setup
    tables =[]
    for i in range(1, 21):
        table = Table(
            number = i,
            seats = 4 if i < 16 else 8
        )
        tables.append(table)
    db.session.add_all(tables)
    db.session.commit()
    
    # Initial food menu setup
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
    db.session.add_all(foods)
    db.session.commit()
    
    # Sample customer setup
    customer = [
        Customer(
        first_name = "Ryan",
        last_name = "Evans",
        phone = "0468426279",
        email = "test@test.com",
        password = bcrypt.generate_password_hash('lwhaus').decode('utf-8'),
    )]
    db.session.add_all(customer)
    db.session.commit()
    
    # Sample booking setup
    booking = Booking(
        date = date.today(),
        time = "12:30",
        pax = 4,
        comment = "Test only",
        table = tables[3],
        customer = customer[0]
    )
    db.session.add(booking)
    db.session.commit()

    # Sample order and association table setup
    order = Order(
            staff = staffs[0],
            table = tables[1],
            date = date.today()
        )
    db.session.add(order)
    db.session.commit()
    receipt = Receipt(
        orders = order,
        payments = payments[1])
    db.session.add(receipt)
    db.session.commit()
    item = [(foods[0], 3), (foods[2], 2)]
    order.generate_order_food(item)
    order.calc_total_price(item)
    db.session.commit()

    
    print('Initial tables seeded')