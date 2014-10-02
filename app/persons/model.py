# coding:utf-8
from app.base import BaseProvider, DomainModel


class PersonProvider(BaseProvider):
    #TODO: create some data_source for it
    data_source = None


class Person(DomainModel, PersonProvider):
    u"""
    Person who will do the work
    """
    # person have a name, name must be a unicode string
    name = None
    # person have a contacts, contacts must be email
    #TODO: make contacts structure for multiple accs, like twi, fb etc
    contacts = None

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


# class QueueGroup(object):
#     u"""
#     Очереди можно объединять в группы
#     """
#     groups = None
#
#     def __init__(self, ):