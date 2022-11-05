from flask import Flask
from config import db, ma, bcrypt, jwt
# from controllers.cards_controller import cards_bp
from controllers.foods_controller import foods_bp
from controllers.auth_controller import auth_bp
from controllers.cli_controller import db_commands
from controllers.auth_controller import auth_bp
from controllers.customers_controller import customers_bp
from marshmallow import ValidationError
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
    
    @app.errorhandler(ValidationError)
    def key_error(err):
        return {'error' : err.messages}, 400

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


    return app


