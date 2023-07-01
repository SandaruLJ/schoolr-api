"""
Module for handling the application's logging functionality

Functions:

    config_logfile() -> None
"""

import os

from logging import FileHandler
from datetime import datetime

from flask import Flask

from schoolr_api.common.constants import LOG_DIR, LOG_FILE_PREFIX, LOG_FILE_DATE_FORMAT


def config_logfile(app: Flask) -> None:
    """Configure app logger with a file handler to write to a file."""
    filename = f'{LOG_FILE_PREFIX}_{datetime.today().strftime(LOG_FILE_DATE_FORMAT)}.log'
    path = f'{app.instance_path}/{LOG_DIR}/{filename}'

    # make log path if it doesn't exist
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    file_handler = FileHandler(path)
    file_handler.setFormatter(app.logger.handlers[0].formatter)

    app.logger.addHandler(file_handler)
