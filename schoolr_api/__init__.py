"""
The main package of the API

Modules:

    db
    common.constants

Functions:

    create_app(test_config) -> object
"""

import os

from flask import Flask

from schoolr_api.resources import api
from schoolr_api.log import config_logfile
from schoolr_api.common.constants import (
    DEV_SECRET_KEY, CONFIG_FILE, LOCAL_DB, APP_NAME
)


def create_app(test_config=None) -> Flask:
    """Create, configure, and return app object"""
    app = Flask(__name__, instance_relative_config=True)

    # Disable strict trailing slash rule for routes
    app.url_map.strict_slashes = False

    # load default config
    app.config.from_mapping(
        SECRET_KEY=DEV_SECRET_KEY,
        MONGO_URI=LOCAL_DB
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile(CONFIG_FILE, silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # bind app to the API
    api.init_app(app)

    # configure logger
    config_logfile(app)

    return app
