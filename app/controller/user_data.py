from flask_restplus import Resource
from flask import request
from ..services.user_data import get_user_data, create_user
from ..services.validate_login_credentials import validate_login_credentials

from ..dto.userdata import UserDataSerializers, ns

_validate_user_login = UserDataSerializers.UserCredentials
_user_registration = UserDataSerializers.UserRegistration
_user_data = UserDataSerializers.UserData


@ns.route("/create-user")
class GetUser(Resource):
    @ns.expect(_user_registration)
    def post(self):
        user_data = request.json
        email = user_data.get('Email')
        phone = user_data.get('PhoneNumber')
        username = user_data.get('UserName')
        password = user_data.get('PasssWord')
        name = user_data.get('FirstName')
        lastname = user_data.get('LastName')
        return create_user(email, phone, username, password, name, lastname)


@ns.route("/get-user-data")
class GetUserData(Resource):
    @ns.expect(_user_data)
    def post(self):
        user_data = request.json
        email = user_data.get('Email')
        phone = user_data.get('PhoneNumber')
        country_code = user_data.get('CountryCode')
        return get_user_data(email, phone, country_code)


@ns.route("/validate-user-login")
class ValidateUserLogin(Resource):
    @ns.expect(_validate_user_login)
    def post(self):
        user_data = request.json
        email = user_data.get('Email')
        username = user_data.get('UserName')
        password = user_data.get('PassWord')
        return validate_login_credentials(email, username, password)
