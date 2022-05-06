from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


class MethodNotAllowed(APIException):
    status_code = 405
    default_code = 'MethodNotAllowed'

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    return response