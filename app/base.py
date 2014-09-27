# coding:utf-8
"""
Black magic
"""
from flask.ext.restful import Resource
from app.locale_app import lc
from abc import ABCMeta
import threading


class LocalizationObject(object):
    """
    Auto localization for all subclass
    """
    pass


class ManagerSingletonABS(LocalizationObject):
    u"""
    Абстрактный класс для всех Одиночек, управляющих чем-либо
    """
    __metaclass__ = ABCMeta
    __singleton_lock = threading.Lock()
    __instance = None
    __objects = [] # It will be bug, if state will be stored in memory like this
    # can be different state in different process (pre-fork\worker web-server)
    #TODO, FIXME: make persistent storage

    def __new__(cls, *args, **kwargs):
        with cls.__singleton_lock:
            if cls.__instance is None:
                cls.__instance = super(ManagerSingletonABS,
                                      cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def get_all_elemens(self):
        u"""
        Получаем список всех подконтрольных элементов
        """
        return self.__objects

    def register(self, el):
        u"""
        Добавляем к списку новый подконтрольный элемент
        """
        with self.__class__.__singleton_lock:
            self.__objects.append(el)

    def un_register(self, el):
        u"""
        Удаляем ненужный подконтрольный элемент
        """
        with self.__class__.__singleton_lock:
            self.__objects.remove(el)


class BaseResource(Resource):
    u"""
    Базовый класс для ресурсов, работающих с менеджерами
    """
    __metaclass__ = ABCMeta

    manager = None

    def get(self, resource_id):
        pass

    def put(self):
        pass

    def delete(self, resource_id):
        pass