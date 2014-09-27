# coding:utf-8


def translate_string(string):
    """
    mock функции перевода строк.
    в будущем будет добавлена реализация перевода всех текстов приложения
    :param string:
    :return:
    """
    return string

# Для сокращенного использования
lc = translate_string


def localize(func):
    """
    Декоратор для локализации doc функции
    :param func:
    :return: func
    """
    if hasattr(func, '__doc__'):
        func.__doc__ = lc(func.__doc__)
    return func