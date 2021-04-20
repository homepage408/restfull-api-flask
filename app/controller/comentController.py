from app.models.user import User
from app import app, db
from kanpai import Kanpai
from app.models.coment import coment, CommentSchema, comment_schema, comments_schema
from app.common.helpers import response
from app.common.middleware import auth, kanpai
from app.common.middleware.kanpai import userRegister
from flask import request, jsonify, make_response
from flask_jwt_extended import *
from flask_restful import Resource
import datetime


class CommentController(Resource):
    def get(self, id=None):
        try:
            if id is None:
                data = coment.query.all()
                if data == []:
                    return response.badRequest([], "Data doesn't exist")
                return response.success(comments_schema.dump(data), "success")
            else:
                data = coment.query.filter_by(id=id).first()
                if data == []:
                    return response.badRequest([], "Data doesn't exist")
                return response.success(comment_schema.dump(data), "success")
        except Exception as e:
            return response.badRequest(e, 'error')

    def post(self,):
        try:
            context = request.json
            craete_coment = coment(
                user_id=context['user_id'], task_id=context['task_id'], comment=context['comment'])
            db.session.add(craete_coment)
            db.session.commit()
            return response.success(comment_schema.dump(craete_coment), "Success")
        except Exception as e:
            return response.badRequest(e, 'error')

    