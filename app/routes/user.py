from app import app, api
from flask import Flask
from app.controller import userController


api.add_resource(userController.controlUser, '/user')
