from app.models.user import User
from app import app, db
from kanpai import Kanpai
from app.common.helpers import response
from app.common.middleware import auth, kanpai
from app.common.middleware.kanpai import userRegister
from flask import request, jsonify, make_response
from flask_jwt_extended import *
from flask_restful import Resource
import datetime


class controlUser(Resource):
    def post(self):
        try:
            context = request.json
            validation_result = userRegister.validate(request.json)
            userEmail = User.query.filter_by(email=context['email']).first()
            if userEmail != None:
                return response.badRequest(userEmail.email, 'email must be unique'), 400

            if validation_result.get('success', False) is False:
                return response.badRequest(validation_result.get('error'), 'error'), 400

            created_user = User(
                name=context['name'], email=context['email'], role=context['role'])
            created_user.setPassword(context['password'])
            db.session.add(created_user)
            db.session.commit()
            return response.success(created_user.fetchall(), 'success'), 201
        except Exception as e:
            return response.badRequest(e, 'error'), 500

    def get(self):
        return response.success('', '')
