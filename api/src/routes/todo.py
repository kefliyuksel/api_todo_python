from flask_restful import Resource, abort, reqparse, fields, marshal_with, marshal
from src.models import db
from src.models.todo import TodoModel

todo_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String
}

todo_list_fields = {
    'count': fields.Integer,
    'todos': fields.List(fields.Nested(todo_fields)),
}

todo_post_parser = reqparse.RequestParser()
todo_post_parser.add_argument('title', type=str, required=True, location=['json'],
                              help='name parameter is required')
todo_post_parser.add_argument('description', type=str, required=True, location=['json'],
                              help='description parameter is required')


def abort_if_todo_doesnt_exist(todo_id, todo):
    if not todo:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class Todo(Resource):
    def get(self, todo_id):
        todo = TodoModel.query.filter_by(id=todo_id).first()
        abort_if_todo_doesnt_exist(todo, todo_id)
        return marshal(todo, todo_fields)

    def delete(self, todo_id):
        todo = TodoModel.query.filter_by(id=todo_id).first()
        abort_if_todo_doesnt_exist(todo, todo_id)
        todo.delete()
        return '', 204

    def put(self, todo_id):
        args = todo_post_parser.parse_args()
        todo = TodoModel.query.filter_by(id=todo_id).first()
        abort_if_todo_doesnt_exist(todo, todo_id)
        todo.update(**args)
        return marshal(todo, todo_fields)

class TodoList(Resource):
    def get(self):
        todos = TodoModel.query.all()
        return marshal({
                'count': len(todos),
                'todos': [marshal(t, todo_fields) for t in todos]
            }, todo_list_fields)
    
    @marshal_with(todo_fields)
    def post(self):
        args = todo_post_parser.parse_args()
        todo = TodoModel(**args)
        todo.save()

        return todo, 201