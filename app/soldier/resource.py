# coding:utf-8
from flask.ext.restful import Resource
from

class SoldierRes(Resource):
    u"""

    """
    def get(self, soldier_id):
        return {}
        # return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}