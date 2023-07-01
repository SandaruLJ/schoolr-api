"""Test module for application factory"""

from schoolr_api import create_app


def test_config():
    """Test passing test config to the factory function."""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
