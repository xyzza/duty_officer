# coding:utf-8
from app.base import LocalizationObject


class Soldier(LocalizationObject):
    u"""
    Боец, тот кто будет смело нести бремя дежурства,
    и храбро бросаться в бой.
    """
    name = None
    contacts = None

    def __init__(self, name, contacts, days):
        """
        :param name: Фио бойца
        :param contacts: Объекты контактов бойца
        :return: None
        """
        self.name = name
        self.contacts = contacts


class SoldierQueue(LocalizationObject):
    u"""
    Очередь(кольцевая) из храбрых бойцов, ожидающий своего часа.
    Все как один готовы к подвигам.
    """

    list_of_soldiers = None

    def add(self, soldier, position=None):
        pass

    def delete(self, soldier):
        pass

    def next(self):
        pass

    def prev(self):
        pass


# class QueueGroup(LocalizationObject):
#     u"""
#     Очереди можно объединять в группы
#     """
#     groups = None
#
#     def __init__(self, ):