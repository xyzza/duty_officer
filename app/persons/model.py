# coding:utf-8
from app.base import BaseProvider, DomainModel, JSONFileSource


class PersonStorage(JSONFileSource):
    u"""Store all data in JSON format in file """
    _source_file = 'app/storage/persons.json'


class PersonProviderMixin(BaseProvider):
    u""" Provider provide CRUD operation API for Person model"""
    data_source = PersonStorage


class PersonMixin(DomainModel, PersonProviderMixin):
    u"""
    Domain model. Simulates the Person object
    """
    # person have a name, name must be a unicode string
    name = None
    # person have a contacts, contacts must be email
    #TODO: make contacts structure for multiple accs, like twi, fb etc
    contacts = None

    @classmethod
    def _load_domain(cls, obj=None, *args, **kwargs):
        """
        implement _load_domain method from PersonProviderMixin
        :param obj:
        :param args:
        :param kwargs:
        :return:
        """
        if obj:
            obj.update(**kwargs)
        return obj if obj else kwargs

    def __init__(self, name, contacts, days):
        """
        :param name: Фио бойца
        :param contacts: Объекты контактов бойца
        :return: None
        """
        self.name = name
        self.contacts = contacts

# class PersonQueue(object):
#     u"""
#     Cycle Queue of persons
#     """
#
#     list_of_soldiers = None
#
#     def add(self, soldier, position=None):
#         pass
#
#     def delete(self, soldier):
#         pass
#
#     def next(self):
#         pass
#
#     def prev(self):
#         pass