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


class controlUser(Resource):
    def post(self):
        try:
            context = request.json
            validation_result = userRegister.validate(request.json)
            if validation_result.get('success', False) is False:
                return response.badRequest(validation_result.get('data'), validation_result.get('error'))

            userEmail = User.query.filter_by(
                email=context['email']).first()
            if userEmail != None:
                return response.badRequest(userEmail.email, 'email must be unique'), 400

            if validation_result.get('success', False) is False:
                return response.badRequest(validation_result.get('error'), 'error'), 400

            created_user = User(
                name=context['name'], email=context['email'], role=context['role'])
            created_user.setPassword(context['password'])
            db.session.add(created_user)
            db.session.commit()
            print(user_schema.dump(created_user))
            return response.success(user_schema.dump(created_user), 'success'), 201
        except Exception as e:
            return response.badRequest(e, 'error'), 500

    @jwt_required()
    def get(self, id=None):
        try:
            user = get_jwt_identity()
            if user.get('role.name') == "supervisor":
                if id is None:
                    data = User.query.all()
                    return response.success(users_schema.dump(data), 'success')
                else:
                    dataFilter = User.query.filter_by(id=id).first()
                    if dataFilter is None:
                        return response.badRequest([], "Data doens't exist")
                    dataUser = user_schema.dump(dataFilter)
                    return response.success(dataUser, '')
            else:
                return response.badRequest([], 'Unauthorization'), 401
        except Exception as e:
            return response.badRequest(e, 'error')

    def put(self, id):
        try:
            context = request.json
            data = User.query.filter_by(id=id).first()
            if data is None:
                return response.badRequest([], "Data doesn't exist")
            else:
                dataEmail = User.query.filter_by(
                    email=context['email']).first()
                if dataEmail is not None:
                    return response.badRequest(context['email'], "email is already in use")

                data.name = context['name']
                data.email = context['email']
                data.role = context['role']

                db.session.commit()

                print(user_schema.dump(data))
                return response.success(user_schema.dump(data), 'success')
        except Exception as e:
            return response.badRequest(e, 'error')

    def delete(self, id):
        try:
            data = User.query.filter_by(id=id).first()
            # print(data.email)
            if data is None:
                return response.badRequest([], "Data doesn't exist")
            else:
                db.session.delete(data)
                db.session.commit()
                return response.success(user_schema.dump(data), 'success delete')
        except Exception as e:
            return response.badRequest(e, 'error')
