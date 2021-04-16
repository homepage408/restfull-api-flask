from app.models.user import User
from app import app, db
from kanpai import Kanpai
# from app.common.helpers import response
from app.common.middleware import auth, kanpai
from app.common.middleware.kanpai import userRegister
from flask import request, jsonify
from flask_jwt_extended import *
from flask_restful import Resource
import datetime


class controlUser(Resource):
    def post(self):
        try:
            context = request.json
            validation_result = userRegister.validate(request.json)
            userEmail = User.query.filter_by(email=context['email']).first()
            # print(userEmail != None)
            if userEmail != None:
                return jsonify({'Message': 'Email harus unique'})

            if validation_result.get('success', False) is False:
                return jsonify({
                    "status": 'error',
                    "error": validation_result.get('error')
                })

            created_user = User(
                name=context['name'], email=context['email'], role=context['role'])
            created_user.setPassword(context['password'])
            db.session.add(created_user)
            db.session.commit()

        except Exception as e:
            return jsonify({
                "status": "Error",
                "error": e
            }), 500

    def get(self):
        return jsonify({
            "data": "data",
            "message": "message"
        })
