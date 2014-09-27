# coding:utf-8
from app.base import LocalizationObject


class Schedule(LocalizationObject):
    u"""
    Класс расписания, показывает расписание для объекта.
    Объектом омжет быть сотрудник, группа сотрудников, работа.
    """
    # schedule build for this object
    obj = None
    # list of ints day numbers
    days = None
    # schedule is actual for obj since start date
    start_date = None
    # and until end date
    stop_date = None

    def __init__(self, obj, start, stop, days):
        self.soldier = obj
        self.days = days
        self.start_date = start
        self.stop_date = stop


class ScheduleExclude(LocalizationObject):
    u"""
    Объект представляет собой исключения в расписании для некоторого объекта
    """
    obj = None
    dates = None

    def __init__(self, obj, dates):
        self.obj = obj
        self.dates = dates