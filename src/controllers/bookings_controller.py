from flask import Blueprint, request, abort
from config import db, query_by_id, not_found_simple
from models.customer import Customer
from models.booking import Booking
# from schemas.customer_schema import CustomerSchema
from schemas.booking_schema import BookingSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import authorization, is_customer
from datetime import date, timedelta
from random import randint
from flask_jwt_extended import jwt_required


bookings_bp = Blueprint('bookings', __name__, url_prefix='/bookings')


## Functions using a lot in this controller
def not_found():
    return {'error': f'Bookings not found.'}, 404
    
# Assigning tables will be updated on the official release. This is for only MVC
def assign_table(pax):
    try:
        if int(pax) <= 4:
            table_id = randint(1, 15)
        else:
            table_id = randint(16, 20)
        return table_id
    except ValueError:
        abort(400, description='Please check the number of pax and try again.')
        
    
#Getting all bookings from the db
@bookings_bp.route('/')
@jwt_required()
def all_bookings():
    authorization()
    stmt = db.select(Booking).order_by(Booking.id)
    bookings = db.session.scalars(stmt)
    return BookingSchema(many=True).dump(bookings), 201
    
    
#Get specific booking with id
@bookings_bp.route('/<int:id>/')
@jwt_required()
def get_one_booking(id):
    authorization()
    booking = query_by_id(Booking, id)
    if booking:
        return BookingSchema().dump(booking)
    else:
        return not_found_simple('Booking')
    

#Get bookings of today
@bookings_bp.route('/today/')
@jwt_required()
def get_today_bookings():
    authorization()
    stmt = db.select(Booking).filter_by(date=date.today())
    booking = db.session.scalars(stmt)
    result = BookingSchema(many=True).dump(booking)
    if len(result) == 0:
        return not_found_simple('Bookings')
    else:
        return result
    
    
#Get bookings of tomorrow
@bookings_bp.route('/tomorrow/')
@jwt_required()
def get_tomorrow_bookings():
    authorization()
    stmt = db.select(Booking).filter_by(date=date.today()+timedelta(days=1))
    booking = db.session.scalars(stmt)
    result = BookingSchema(many=True).dump(booking)
    if len(result) == 0:
        return not_found_simple('Bookings')
    else:
        return result
    
    
#search bookings by date
@bookings_bp.route('/<string:year>/<string:month>/<string:day>')
@jwt_required()
def search_bookings_date(year, month, day):
    authorization()
    date_to_search = '-'.join([year, month, day])
    stmt = db.select(Booking).filter_by(date=date_to_search)
    bookings = db.session.scalars(stmt)
    result = BookingSchema(many=True).dump(bookings) # result can be none or one or a lot
    if len(result) == 0:
        return not_found_simple('Bookings')
    else:
        return result


#Get my bookings
@bookings_bp.route('/mybookings/')
@jwt_required()
def get_my_bookings():
    is_customer()
    stmt = db.select(Booking).filter_by(customer_id=get_jwt_identity())
    bookings = db.session.scalars(stmt)
    result = BookingSchema(many=True).dump(bookings)
    if len(result) == 0:
        return not_found_simple('Bookings')
    else:
        return result


# Create a new booking by customer
@bookings_bp.route('/new', methods=['POST'])
@jwt_required()
def create_booking():
    data_booking = BookingSchema().load(request.json)
    booking = Booking(
        date = data_booking['date'], # check again
        time = data_booking['time'], # check again
        pax = data_booking['pax'],
        table_id = assign_table(data_booking['pax']),
        comment = data_booking.get('comment'),
        customer_id = get_jwt_identity()
    )
    db.session.add(booking)
    customer = query_by_id(Customer, get_jwt_identity())
    customer.visited += 1 # Visited records
    db.session.commit()
    return BookingSchema().dump(booking), 201