from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()


    ## Functions using a lot in this app
# when you want to query by id and get only one result
def query_by_id(table, filter):
    stmt = db.select(table).filter_by(id=filter)
    order = db.session.scalar(stmt)
    return order


def not_found_simple(object):
    return {'error': f'{object} not found.'}, 404


def not_found(table, id):
    return {'error': f'{table} {id} not found. Please try again'}, 404