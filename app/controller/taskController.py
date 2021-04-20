from app.models.user import User
from app import app, db
from kanpai import Kanpai
from app.models.task import Task, TaskSchema, tasks_schema, task_schema
from app.common.helpers import response
from app.common.middleware import auth, kanpai
from app.common.middleware.kanpai import inputTask
from flask import request
from flask_jwt_extended import *
from flask_restful import Resource
import datetime


class TaskController(Resource):
    def post(self):
        try:
            context = request.json
            validation_result = inputTask.validate(request.json)
            if validation_result.get('success', False) is False:
                return response.badRequest(validation_result.get('data'), validation_result.get('error'))
            create_task = Task(user_id=context['user_id'], title=context['title'],
                               description=context['description'], duedate=context['duedate'],
                               status=context['status'])
            db.session.add(create_task)
            db.session.commit()
            data = task_schema.dump(create_task)
            return response.success(data, 'success')
        except Exception as e:
            return response.badRequest(e, 'error')

    @jwt_required()
    def get(self,):
        try:
            data = Task.query.all()
            return response.success(tasks_schema.dump(data), 'success')
        except Exception as e:
            return response.badRequest(e, 'error')

    def put(self, id):
        try:
            context = request.json
            data = Task.query.filter_by(id=id).first()
            if data is None:
                return response.badRequest([], "Data doens't exist")
            else:
                data.user_id = context['user_id']
                data.title = context['title']
                data.description = context['description']
                data.duedate = context['duedate']
                data.status = context['status']

                db.session.commit()
                return response.success(task_schema.dump(data), 'success')
        except Exception as e:
            return response.badRequest(e, 'error')

    def delete(self, id):
        try:
            data = Task.query.filter_by(id=id).first()
            if data is None:
                return response.badRequest([], "Data doens't exist")
            else:
                db.session.delete(data)
                db.session.commit()
                return response.success(task_schema.dump(data), 'success')
        except Exception as e:
            return response.badRequest(e, 'error')
