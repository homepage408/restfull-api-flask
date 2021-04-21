from app.models.user import User
from app import app, db
from kanpai import Kanpai
from app.models.user import User, UserForNestedSchema
from app.models.task import Task, TaskSchema, tasks_schema, task_schema,  TaskNestedSchema
from app.models.coment import coment, comment_schema, comments_schema, CommentForNestedSchema
from app.common.helpers import response
from app.common.middleware import auth, kanpai
from app.common.middleware.kanpai import inputTask
from flask import request, jsonify
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
    def get(self, id=None):
        try:
            if id is None:
                # data = db.session.query(Task.user_id, Task.title, Task.description, Task.duedate, Task.status,coment.id,
                #                         coment.user_id, coment.task_id, coment.comment).join(coment).filter(Task.id == coment.task_id).distinct()
                dataTask = Task.query.all()
                task_new_schema = TaskNestedSchema(many=True)
                output = task_new_schema.dump(dataTask)
                # print(output)
                # print(tasks_nested_schema.dump(data))
                # print(tasks_schema.dump(data))
                # return response.success(output, 'success')
                return jsonify({'message':output})

            else:
                pass
                # data = Task.query.filter_by(id=id).first()
                # if data is None:
                #     return response.badRequest([], "Data doens't exist")

                # return response.success(task_schema.dump(data), 'success')
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
