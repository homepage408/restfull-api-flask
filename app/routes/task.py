from app import app, api
from flask import Flask
from app.controller import taskController

api.add_resource(taskController.TaskController, '/task',
                 methods=['POST', 'GET'], endpoint='task')
api.add_resource(taskController.TaskController, '/task/<int:id>',
                 methods=['DELETE','PUT'], endpoint='task-edit')
