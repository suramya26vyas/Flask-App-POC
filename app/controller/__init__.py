from flask_restplus import Api
from ..error_handlers.exceptions import InputKeywordError, DataBaseError
from werkzeug.exceptions import HTTPException
from flask import Blueprint
from ..controller.otp import ns as otp
from ..controller.user_data import ns as user_data
from ..controller.web_scrap import ns as scraped_data
from ..controller.fb_scrap_selenium import ns as fb_data

from requests.exceptions import ConnectionError
from error_codes import ERROR_CODES
import sys, traceback
# class Api(_Api):
#     def error_router(self, original_handler, e):
#         # Override original error_router to only handle HTTPExceptions.
#         if self._has_fr_route() and isinstance(e, HTTPException):
#             try:
#                 # Use Flask-RESTful's error handling method
#                 return self.handle_error(e)
#             except Exception:
#                 # Fall through to original handler (i.e. Flask)
#                 pass
#         return original_handler(e)


bp = Blueprint('Flask-POC', __name__, url_prefix='/api')
web_scraping_bp = Blueprint('Web-scrapping', __name__, url_prefix='/api_ws')
fb_scraping_bp = Blueprint('Facebook', __name__, url_prefix='/api_fb')


api = Api(bp, catch_all_404s=True)

api.add_namespace(otp)
api.add_namespace(user_data)

api_ws = Api(web_scraping_bp)
api_ws.add_namespace(scraped_data)

api_fb = Api(fb_scraping_bp)
api_fb.add_namespace(fb_data)


@api_ws.errorhandler(HTTPException)
@api_fb.errorhandler(HTTPException)
@api.errorhandler(HTTPException)
def http_exception_handler(error: HTTPException):
    """ HTTP exception handler"""
    exc_type, exc_value, exc_traceback = sys.exc_info()
    message = "HTTPException occurred."
    error_data = {'message': message}
    if exc_traceback:
        exception_name = type(exc_type).__name__
        if type(exc_type).__name__ == 'type':
            exception_name = exc_type.__name__
        message = exception_name + ": " + str(error.description)
        error_data = {
            "exception": exception_name,
            "message": message
        }
    return error_data, error.code


@api_ws.errorhandler(ConnectionError)
@api_fb.errorhandler(ConnectionError)
@api_ws.errorhandler(ConnectionError)
def default_error_handler(error):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    error_data = {}
    if exc_traceback:
        exception_name = type(exc_type).__name__
        if type(exc_type).__name__ == 'type':
            exception_name = exc_type.__name__
        message = exception_name + ": " + str(exc_value)
        error_data = {
            "exception": exception_name,
            "message": message
        }
    return error_data, ERROR_CODES.get("ConnectionError")


@api.errorhandler(DataBaseError)
def database_error_handler(error):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exception_name = ''
    exception_data = traceback.format_exc().splitlines()
    file_data = exception_data[1].split(",")
    file_path = file_data[0].lstrip("  File ")
    if type(exc_type).__name__ == 'type':
        exception_name = exc_type.__name__
    error_data = {
        "traceback": file_path,
        "exception_caught": exception_name,
        "message": error.message
    }
    return error_data, error.status_code


@api.errorhandler(InputKeywordError)
def default_error_handler(error):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exception_name = ''
    exception_data = traceback.format_exc().splitlines()
    file_data = exception_data[1].split(",")
    file_path = file_data[0].lstrip("  File ")
    if type(exc_type).__name__ == 'type':
        exception_name = exc_type.__name__
    error_data = {
        "traceback": file_path,
        "exception_caught": exception_name,
        "message": error.message,
    }
    return error_data, error.status_code


@api.errorhandler
def default_error_handler(error):
    """Default error handler"""
    return {'message': str(error.message)}, getattr(error, 'code', 500)
