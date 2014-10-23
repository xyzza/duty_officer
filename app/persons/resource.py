# coding:utf-8
from flask import request
from flask.ext.restful import Resource, reqparse
from model import PersonMixin


class PersonRes(Resource):
    u"""
    Person REST resource
    """

    def get(self, person_id):
        u"""
        get one Person object by it id
        """
        return PersonMixin.get(person_id)

    def put(self, person_id):
        u"""
        update one Person with new values from form
        """
        return PersonMixin.update(person_id, **request.form)

    def delete(self, person_id):
        u"""
        delete one Person object by it id
        """
        try:
            return PersonMixin.delete(person_id)
        except KeyError:
            return "Person with this key not found!"


class PersonListRes(Resource):
    u"""
    Person REST resource for create and list operations
    """
    def post(self):
        u"""
        Create new Person object
        :return:
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=unicode)
        parser.add_argument('contacts', type=unicode)
        return PersonMixin.create(**parser.parse_args()), 201

    def get(self):
        u"""
        Return list of all Persons
        """
        return PersonMixin.records()