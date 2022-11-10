from flask import Flask, abort, jsonify
from config import db, ma, bcrypt, jwt
# from controllers.cards_controller import cards_bp
from controllers.foods_controller import foods_bp
from controllers.auth_controller import auth_bp
from controllers.cli_controller import db_commands
from controllers.auth_controller import auth_bp
from controllers.customers_controller import customers_bp
from controllers.bookings_controller import bookings_bp
from controllers.orders_controller import orders_bp
from controllers.tables_controller import tables_bp
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
import os




def create_app():
    app = Flask(__name__)

    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)}, 400
    
    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404
    
    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401
    
    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required.'}, 400

    # @app.errorhandler(TypeError)
    # def type_error(err):
    #     return {'error': f'{err}'}, 400
    
    # @app.errorhandler(DataError)
    # def type_error(err):
    #     return {'error': f'{err}'}, 400
    
    @app.errorhandler(ValidationError)
    def validate_error(err):
        return {'error' : err.messages}, 400
    
    @app.errorhandler(IntegrityError)
    def Integrity_error(err):
        return {'error' : f'{err}'}, 400
    
    @app.errorhandler(AttributeError)
    def attribute_error(err):
        return {'error' : str(err)}, 400
    


    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['JSON_SORT_KEYS'] = False

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(customers_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(db_commands)
    app.register_blueprint(foods_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(bookings_bp)
    app.register_blueprint(tables_bp)


    return app


