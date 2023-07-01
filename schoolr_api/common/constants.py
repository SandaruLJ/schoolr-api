"""Module for storing constants used in the API."""

# app configuration
APP_NAME = 'schoolr-api'
SECRET_KEY = 'SECRET_KEY'
MONGO_URI = 'MONGO_URI'

DEV_SECRET_KEY = 'dev'
LOCAL_DB = 'mongodb://localhost:27017/dev'

CONFIG_FILE = 'config.py'

# log configuration
LOG_DIR = 'logs'
LOG_FILE_DATE_FORMAT = '%Y-%m-%d'
LOG_FILE_PREFIX = APP_NAME

# API and route configuration
API_PREFIX = 'api'
API_VERSION = 'v1'
PREFIX = f'/{API_PREFIX}/{API_VERSION}'
