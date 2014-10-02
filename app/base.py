# coding:utf-8
"""
Black magic
"""


class DomainModel(object):
    pass


class BaseProvider(object):
    u"""
    BASE Provider class for CRUD operations
    """
    # Encapsulate data source - it can be SQL DB, or file or else
    data_source = None

    @classmethod
    def create(cls, *args, **kwargs):
        return {1: u"created mock object from provider"}
        # return cls.data_source.create(*args, **kwargs)

    @classmethod
    def update(cls, obj_id):
        return {1: u"updated mock object from provider"}
        # return cls.data_source.update(obj_id)

    @classmethod
    def get(cls, obj_id):
        return {1: u"mock object from provider"}
        # return cls.data_source.get(obj_id)

    @classmethod
    def records(cls):
        return [{1: u"mock object from provider records"}, ]
        # return cls.data_source.records()

    @classmethod
    def delete(cls, obj_id):
        return {1: u"deleted mock object from provider"}
        # return cls.data_source.delete(obj_id)