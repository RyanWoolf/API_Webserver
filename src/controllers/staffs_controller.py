from flask import Blueprint, request
from config import db, bcrypt
from models.staff import Staff
from schemas.staff_schema import StaffSchema
from controllers.auth_controller import authorization
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta

