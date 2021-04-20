from app import app, api
from flask import Flask
from app.controller import comentController

api.add_resource(comentController.CommentController, '/comment',
                 methods=['POST', 'GET'], endpoint='comment')

api.add_resource(comentController.CommentController, '/comment/<int:id>',
                 methods=['GET', 'PUT', 'DELETE'], endpoint='comment-edit')
