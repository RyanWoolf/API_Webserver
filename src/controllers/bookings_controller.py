from flask import Blueprint, request, abort
from config import db, query_by_id, not_found_simple, not_found
from models.customer import Customer
from models.booking import Booking
from schemas.booking_schema import BookingSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import authorization, is_customer, authorization_admin
from datetime import date, timedelta
from random import randint
from flask_jwt_extended import jwt_required


bookings_bp = Blueprint('bookings', __name__, url_prefix='/bookings')

    
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
@bookings_bp.route('/<string:year>/<string:month>/<string:day>/')
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


#Get my bookings by customer
@bookings_bp.route('/mybookings/')
@jwt_required()
def get_my_bookings():
    is_customer()
    stmt = db.select(Booking).filter_by(customer_id=get_jwt_identity())
    bookings = db.session.scalars(stmt)
    result = BookingSchema(many=True, exclude=['customer_id', 'customer']).dump(bookings)
    if len(result) == 0:
        return not_found_simple('Bookings')
    else:
        return result


# Create a new booking by customer
@bookings_bp.route('/new/', methods=['POST'])
@jwt_required()
def create_booking():
    is_customer()
    data_booking = BookingSchema().load(request.json)
    booking = Booking(
        date = data_booking['date'], # Will be updated in the official release
        time = data_booking['time'], # Will be updated in the official release
        pax = data_booking['pax'],
        table_id = assign_table(data_booking['pax']),
        comment = data_booking.get('comment'),
        customer_id = get_jwt_identity()
    )
    db.session.add(booking)
    customer = query_by_id(Customer, get_jwt_identity())
    customer.visited += 1 # Visited records
    db.session.commit()
    return BookingSchema(exclude=['customer_id']).dump(booking), 201


# Create a new booking by admin
@bookings_bp.route('/new/admin/', methods=['POST'])
@jwt_required()
def create_booking_by_admin():
    authorization_admin()
    data_booking = BookingSchema().load(request.json)
    booking = Booking(
        date = data_booking['date'], # Will be updated in the official release
        time = data_booking['time'], # Will be updated in the official release
        pax = data_booking['pax'],
        table_id = assign_table(data_booking['pax']),
        comment = data_booking.get('comment'),
        customer_id = data_booking['customer_id']
    )
    db.session.add(booking)
    customer = query_by_id(Customer, booking.customer_id)
    customer.visited += 1 # Visited records
    db.session.commit()
    return BookingSchema().dump(booking), 201



#Modify booking. Only accessible through id
@bookings_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_customer(id):
    is_customer()
    booking = query_by_id(Booking, id)
    data = BookingSchema().load(request.json)
    if booking:
        booking.date = data.get('date') or booking.date
        booking.time = data.get('time') or booking.time
        booking.pax = data.get('pax') or booking.pax
        booking.comment = data.get('comment') or booking.comment
        db.session.commit()
        return BookingSchema(exclude=['customer_id']).dump(booking)
    else:
        return not_found('Booking', id)
    
    
## Delete a booking
@bookings_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_booking(id):
    authorization_admin()
    booking = query_by_id(Booking, id)
    if booking:
        db.session.delete(booking)
        db.session.commit()
        return {'msg': f'Booking ID {id} deleted successfully'}
    return not_found('Booking', id)