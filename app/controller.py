# coding:utf-8
from flask import Flask
from flask.ext.restful import Api
from app.persons.resource import PersonRes, PersonListRes


app = Flask(__name__)
api = Api(app)


api.add_resource(PersonListRes, '/persons')
api.add_resource(PersonRes, '/person/<string:person_id>')