from flask import Blueprint, request, url_for, redirect
from config import db, query_by_id, not_found
from models.food import Food
from schemas.food_schema import FoodSchema
from controllers.auth_controller import authorization_admin
from flask_jwt_extended import jwt_required


foods_bp = Blueprint('foods', __name__, url_prefix='/foods')
tags = ('gf', 'df', 'v')


#Getting all food from the menu
@foods_bp.route('/')
def all_foods():
    stmt = db.select(Food).order_by(Food.id)
    foods = db.session.scalars(stmt)
    # print(FoodSchema(many=True).dump(foods))
    return FoodSchema(many=True).dump(foods), 201
    
    
#Get specific food with id
@foods_bp.route('/<int:id>/')
def get_one_food(id):
    food = query_by_id(Food, id)
    if food:
        return FoodSchema().dump(food)
    else:
        return not_found('Food', id)
    
    
#search foods with a tag(GF, DF, V)
@foods_bp.route('/<string:tag>/')
def search_food(tag):
    if not tag.lower() in tags:
        return {'error': 'Failed to search. Please check the tag and try again.'}, 404
    else:
        if tag.lower() == 'gf':
            stmt = db.select(Food).filter_by(is_gf=True)
            food = db.session.scalars(stmt)
        elif tag.lower() == 'df':
            stmt = db.select(Food).filter_by(is_df=True)
            food = db.session.scalars(stmt)
        elif tag.lower() == 'v':
            stmt = db.select(Food).filter_by(is_v=True)
            food = db.session.scalars(stmt)
        return FoodSchema(many=True, only=['name', 'price']).dump(food)


#search foods with two tags(GF, DF, V)
@foods_bp.route('/<string:tag1>/<string:tag2>')
def search_food_tags(tag1, tag2):
    tag1, tag2 = tag1.lower(), tag2.lower()
    if tag1 not in tags or tag2 not in tags:
        return {'error': 'Failed to search. Please check the tag and try again.'}, 404
    elif tag1 == tag2: # If you put two same tags, it redirects to search_food
        return redirect(url_for('foods.search_food', tag = tag1))
    rest = list(tags)
    rest.remove(tag1)
    rest.remove(tag2)
    if 'v' in rest:
        stmt = db.select(Food).filter_by(is_gf=True, is_df=True)
        food = db.session.scalars(stmt)
    elif 'gf' in rest:
        stmt = db.select(Food).filter_by(is_df=True, is_v=True)
        food = db.session.scalars(stmt)
    elif 'df' in rest:
        stmt = db.select(Food).filter_by(is_v=True, is_gf=True)
        food = db.session.scalars(stmt)
    return FoodSchema(many=True, only=['name', 'price']).dump(food)


#Add new food in the DB, only admin is allowed to do this
@foods_bp.route('/', methods=['POST'])
@jwt_required()
def add_food():
    authorization_admin()
    data = FoodSchema().load(request.json)
    food = Food(
        name = data['name'],
        price = data['price'],
        is_gf = data.get('is_gf'),
        is_df = data.get('is_df'),
        is_v = data.get('is_v'),
    )
    db.session.add(food)
    db.session.commit()
    return FoodSchema().dump(food), 201


#Delete food from the DB. For safety reasons, only accessible through id
@foods_bp.route('/<int:id>/', methods = ['DELETE'])
@jwt_required()
def delete_one_food(id):
    authorization_admin()
    food = query_by_id(Food, id)
    if food:
        db.session.delete(food)
        db.session.commit()
        return {'msg': f'Food {food.name} deleted successfully'}
    else:
        return not_found('Food', id)


#Modify food. Only accessible through id
@foods_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_food(id):
    authorization_admin()
    food = query_by_id(Food, id)
    data = FoodSchema().load(request.json)
    if food:
        food.name = data.get('name') or food.name
        food.price = data.get('price') or food.price
        food.is_gf = data.get('is_gf') if request.json.get('is_gf') is not None else food.is_gf
        food.is_df = data.get('is_df') if request.json.get('is_df') is not None else food.is_df
        food.is_v = data.get('is_v') if request.json.get('is_v') is not None else food.is_v
        db.session.commit()
        return FoodSchema().dump(food)
    else:
        return not_found('Food', id)