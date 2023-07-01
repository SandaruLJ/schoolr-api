"""Configuration for pytest"""

import pytest

from flask import Flask

from schoolr_api import create_app


@pytest.fixture
def app() -> Flask:
    """Provide an instance of the Flask app."""
    return create_app()
