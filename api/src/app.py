from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from src.routes.todo import Todo, TodoList

from .config import app_config
from .models import db

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    db.init_app(app)

    api = Api(app)
    
    api.add_resource(TodoList, '/todos')
    api.add_resource(Todo, '/todos/<todo_id>')

    return app
