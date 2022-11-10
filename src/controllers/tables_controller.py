from flask import Blueprint, request
from config import db, query_by_id, not_found
from models.table import Table
from schemas.table_schema import TableSchema
from controllers.auth_controller import authorization_admin
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError, DataError


tables_bp = Blueprint('tables', __name__, url_prefix='/tables')



def table_number(number):
    stmt = db.select(Table).filter_by(number=number)
    table = db.session.scalar(stmt)
    return table


#Getting all tables from the db
@tables_bp.route('/')
@jwt_required()
def all_tables():
    stmt = db.select(Table).order_by(Table.number)
    tables = db.session.scalars(stmt)
    return TableSchema(many=True).dump(tables), 201
    
    
#get a table with table number
@tables_bp.route('/<int:number>/')
@jwt_required()
def get_table(number):
    stmt = db.select(Table).filter_by(number=number)
    table = db.session.scalar(stmt)
    if table:
        return TableSchema().dump(table)
    else:
        return not_found('Table', number)


#Add new table in the DB, only admin is allowed to do this
@tables_bp.route('/', methods=['POST'])
@jwt_required()
def add_table():
    authorization_admin()
    data = TableSchema().load(request.json)
    try:    
        table = Table(
        number = data['number'],
        seats = data['seats'])
        db.session.add(table)
        db.session.commit()
        return TableSchema().dump(table), 201
    except IntegrityError:
        return {'error': f'Table number {table.number} already in use'}


#Delete table from the DB. For safety reasons, only accessible through id
@tables_bp.route('/<int:id>/', methods = ['DELETE'])
@jwt_required()
def delete_one_table(id):
    authorization_admin()
    table = query_by_id(Table, id)
    if table:
        db.session.delete(table)
        db.session.commit()
        return {'msg': f'Table ID: {table.id}, Number: {table.number} deleted successfully'}
    else:
        return not_found('Table', id)


#Modify table. Only accessible through number
@tables_bp.route('/<int:number>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_table(number):
    authorization_admin()
    stmt = db.select(Table).filter_by(number=number)
    table = db.session.scalar(stmt)
    data_table = TableSchema().load(request.json)
    try:
        if table:
            new_table = data_table.get('number')
            if new_table:
                if not table_number(new_table) or new_table == number:
                    table.number = new_table or table.number
                    table.seats = data_table.get('seats') or table.seats
                    db.session.commit()
                else:
                    return {'error': f'Table number {table.number} already in use'}, 400
            return TableSchema().dump(table)
        else:
            return not_found('Table', number)
    except DataError:
        return {'error': f'Wrong input format. Please try again'}, 400