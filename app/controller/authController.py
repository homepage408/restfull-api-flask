from app.models.user import User
from app import app, db
from kanpai import Kanpai
from app.models.user import User, UserSchema, users_schema, user_schema
from app.common.helpers import response
from app.common.middleware import auth, kanpai
from app.common.middleware.kanpai import userRegister
from flask import request, jsonify, make_response
from flask_jwt_extended import *
from flask_restful import Resource
import datetime


class AuthController(Resource):
    def post(self):
        try:
            context = request.json
            data = User.query.filter_by(email=context['email']).first()
            if data is None:
                return response.badRequest("", "Email doens't exis")

            if not data.checkPassword(context['password']):
                return response.badRequest("", "Password salah")

            user = user_schema.dump(data)
            return response.success(user, auth.generateJwt(user))
        except Exception as e:
            return response.badRequest(e, 'error')
