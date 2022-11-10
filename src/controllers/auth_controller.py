from flask import Blueprint, request, abort
from config import db, bcrypt, query_by_id
from datetime import timedelta
from models.staff import Staff
from schemas.staff_schema import StaffSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


# CHeck if you're a customer
def is_customer():
    id = get_jwt_identity()
    if int(id) < 100:
        return abort(401, description='No Access to customer page.')

# Check if you're a staff
def authorization(): # check again please
    staff_id = get_jwt_identity()
    if int(staff_id) > 100:
        abort(401, description='Only staff members allowed')
        
# Check if you're an admin
def authorization_admin():
    staff_id = get_jwt_identity()
    staff = query_by_id(Staff, staff_id)
    if not staff.is_admin:
        abort(401, description='Only admins allowed')


#Login staff section
@auth_bp.route('/login/', methods=['POST'])
def auth_login():
    stmt = db.select(Staff).filter_by(login_id=request.json['login_id'])
    staff = db.session.scalar(stmt)
    if staff and bcrypt.check_password_hash(staff.password, request.json['password']):
        token = create_access_token(identity=str(staff.id), expires_delta=timedelta(days=1))
        return {'login_id': staff.login_id, 'token': token}, 200 
    else:
        return {'error': 'Invalid name or password'}, 401


#Register staff section
@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    try:
        staff = Staff(
            login_id=request.json['login_id'],
            password=bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
            staff_name=request.json.get('staff_name')
        )
        db.session.add(staff)
        db.session.commit()
        token = create_access_token(identity=str(staff.id), expires_delta=timedelta(days=1))
        return {'msg': f'Login ID: {staff.login_id} registered.', 'token': f'{token}'}, 201
    except IntegrityError:
        return {'error': 'Login Id already in use. Please try again.'}, 409
    
    
#List all staff
@auth_bp.route('/staffs/')
@jwt_required()
def get_staffs():
    authorization_admin()
    stmt = db.select(Staff).order_by(Staff.id)
    users = db.session.scalars(stmt)
    return StaffSchema(many=True, exclude=['password']).dump(users)