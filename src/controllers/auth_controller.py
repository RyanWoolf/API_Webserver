from flask import Blueprint, request, abort
from config import db, bcrypt
from datetime import timedelta
from models.staff import Staff
from schemas.staff_schema import StaffSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity



auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def authorization():
    staff_id = get_jwt_identity()
    stmt = db.select(Staff).filter_by(id=staff_id)
    staff = db.session.scalar(stmt)
    if not staff.is_admin:
        abort(401)




@auth_bp.route('/login/', methods=['POST'])
def auth_login():
    stmt = db.select(Staff).filter_by(login_id=request.json['login_id'])
    staff = db.session.scalar(stmt)
    if staff and bcrypt.check_password_hash(staff.password, request.json['password']):
        token = create_access_token(identity=str(staff.id), expires_delta=timedelta(days=1))
        return {}
    else:
        return {'error': 'Invalid name or password'}, 401

@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    try:
        staff = Staff(
            login_id=request.json['login_id'],
            password=bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
            name=request.json.get('name')
        )
        db.session.add(staff)
        db.session.commit()
        return StaffSchema(exclude=['password']).dump(staff), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409
    
@auth_bp.route('/staffs/')
def get_staffs():
    stmt = db.select(Staff)
    users = db.session.scalars(stmt)
    return StaffSchema(many=True, exclude=['password']).dump(users)