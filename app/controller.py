# coding:utf-8
from app import app
from flask import request
from flask.ext.restful import Resource, Api

api = Api(app)


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(TodoSimple, '/todo/<int:todo_id>', endpoint='todo_ep')