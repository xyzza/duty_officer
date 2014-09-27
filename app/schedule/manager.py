# coding:utf-8
from app.base import ManagerSingletonABS


class ScheduleManager(ManagerSingletonABS):
    u"""
    Одиночка, управляющий всеми расписаниями
    """


class ScheduleExcludeManager(ManagerSingletonABS):
    u"""
    Одиночка, управляющий всеми исключениями расписаний
    """