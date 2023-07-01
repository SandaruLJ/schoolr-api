"""
This package contains the API and its routes, along with the resources
"""

from flask_restful import Api

from schoolr_api.common.constants import PREFIX

from schoolr_api.resources.health import Health


api = Api(prefix=PREFIX)

api.add_resource(Health, '/health')
