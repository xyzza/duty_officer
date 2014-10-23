# coding:utf-8
"""
Black magic
"""
import json


class DomainModel(object):
    pass


class BaseProvider(object):
    u"""
    BASE Provider class for CRUD operations
    """
    # Encapsulate data source - it can be SQL DB, or file or else
    data_source = None

    @classmethod
    def _load_domain(cls, obj=None, *args, **kwargs):
        """
        (Fabric method?)
        This method fill domain model
        must be defined in subclasses
        :rtype object
        """

        raise NotImplementedError

    @classmethod
    def create(cls, *args, **kwargs):
        obj = cls._load_domain(*args, **kwargs)
        return cls.data_source.put_to_persistent(obj)

    @classmethod
    def update(cls, obj_id, *args, **kwargs):
        obj = cls.data_source.get_from_persistent(obj_id)
        obj = cls._load_domain(obj, *args, **kwargs)
        return cls.data_source.put_to_persistent(obj)

    @classmethod
    def get(cls, obj_id):
        raw = cls.data_source.get_from_persistent(obj_id)
        return cls._load_domain(raw)

    @classmethod
    def records(cls):
        return cls.data_source.get_all_from_persistent()

    @classmethod
    def delete(cls, obj_id):
        return cls.data_source.delete_from_persistent(obj_id)


class JSONFileSource(object):
    u"""
    That Source store data in the dict
    dict serializes to JSON, and then stored in file
    """
    # all rows
    _state = {}
    _source_file = None
    __updated = True

    @classmethod
    def _save_to_file(cls):
        _state = json.dumps(cls._state)
        with open(cls._source_file, "w") as f:
            f.write(_state)

    @classmethod
    def _read_from_file(cls):
        if cls.__updated:
            with open(cls._source_file, "r") as f:
                _state = f.read()
                try:
                    cls._state = json.loads(_state)
                except ValueError:
                    cls._state = {}
                else:
                    cls.__updated = False

    @classmethod
    def put_to_persistent(cls, object_dict):
        cls._read_from_file()
        object_dict.setdefault('_id', len(cls._state) + 1)
        obj = cls._state.setdefault(object_dict['_id'], object_dict)
        obj.update(**object_dict)
        cls._save_to_file()
        cls.__updated = True
        return obj

    @classmethod
    def get_from_persistent(cls, object_id):
        cls._read_from_file()
        return cls._state.get(object_id)

    @classmethod
    def get_all_from_persistent(cls):
        cls._read_from_file()
        return cls._state.values()

    @classmethod
    def delete_from_persistent(cls, object_id):
        cls._read_from_file()
        obj = cls._state[object_id]
        del cls._state[object_id]
        cls._save_to_file()
        return obj