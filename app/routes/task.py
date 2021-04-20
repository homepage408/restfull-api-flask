from app import app, api
from flask import Flask
from app.controller import taskController

api.add_resource(taskController.TaskController, '/task',
                 methods=['POST', 'GET', 'DELETE'], endpoint='task')
api.add_resource(taskController.TaskController, '/task/del/<int:id>',
                 methods=['DELETE'], endpoint='task-delete')
