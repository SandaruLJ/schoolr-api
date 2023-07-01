"""
This module contains resources for health checking endpoints

Classes:

    Health
"""

from flask_restful import Resource


class Health(Resource):
    """
    Resource class for health endpoints

    Methods:

        get()
    """

    def get(self):
        """Return a message indicating the application is healthy."""
        return {'message': 'Healthy'}
