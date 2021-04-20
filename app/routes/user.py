from app import app, api
from flask import Flask
from app.controller import userController, authController


api.add_resource(userController.controlUser, '/user',
                 methods=['GET', 'POST'], endpoint='users')
api.add_resource(userController.controlUser,
                 '/user/<email>', methods=['GET'], endpoint='user')
api.add_resource(authController.AuthController, '/login',
                 methods=['POST'], endpoint='login')
