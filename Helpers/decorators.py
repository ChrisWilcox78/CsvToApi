from functools import wraps
from mongoengine import connect
from os import environ
from bson.errors import InvalidId
from mongoengine.queryset import DoesNotExist
from werkzeug.exceptions import NotFound


DEFAULT_MONGO_HOST = "localhost"
DEFAULT_MONGO_PORT = "27017"
DEFAULT_DB_NAME = "entities"


def db_connect(fn):
    """
    Connects to the mongo database server
    """
    @wraps(fn)
    def decorator(*args, **kwargs):
        connect(environ.get("MONGO_DB_NAME", DEFAULT_DB_NAME), host=environ.get("MONGO_HOST", DEFAULT_MONGO_HOST),
                port=int(environ.get("MONGO_PORT", DEFAULT_MONGO_PORT)))
        return fn(*args, **kwargs)

    return decorator


def treat_not_found_as_none(fn):
    """
    Handles the exceptions thrown when a document cannot be found and returns None.
    """
    @wraps(fn)
    def decorator(*args, **kwargs):
        try:
            rval = fn(*args, **kwargs)
        except (InvalidId, DoesNotExist):
            return None
        return rval
    return decorator


def treat_none_as_404(fn):
    """
    Raises werkzeug.exceptions.NotFound if the wrapped function returns None.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        rval = fn(*args, **kwargs)
        if rval is None:
            raise NotFound()
        return rval
    return wrapper
