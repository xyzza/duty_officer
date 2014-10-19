# coding:utf-8
from flask import request
from flask.ext.restful import Resource, reqparse
from model import Person


class PersonRes(Resource):
    u"""
    Person REST resource
    """

    def get(self, person_id):
        return Person.get(person_id)

    def put(self, person_id):
        return Person.update(person_id, **request.form)

    def delete(self, person_id):
        try:
            return Person.delete(person_id)
        except KeyError:
            return "Person with this key not found!"


class PersonListRes(Resource):
    u"""
    """
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=unicode)
        parser.add_argument('contacts', type=unicode)
        return Person.create(**parser.parse_args()), 201

    def get(self):
        return Person.records()