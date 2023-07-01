"""
Module for making connection with the database

Functions:

    get_database() -> object
"""

from flask import current_app, g
from flask_pymongo import PyMongo
from flask_pymongo.wrappers import Database
from werkzeug.local import LocalProxy


def get_db() -> Database:
    """Create and return database instance.""" 
    database = getattr(g, "_database", None)

    if database is None:
        database = g._database = PyMongo(current_app).db

    return database


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)
