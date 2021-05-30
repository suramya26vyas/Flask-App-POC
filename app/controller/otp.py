from flask_restplus import Resource
from flask import request
from ..services.otp import send_otp, verification
from ..dto.otp import OTPSerializers, ns

_send_otp = OTPSerializers.UserData


@ns.route("/send-otp")
class SendOTP(Resource):
    @ns.expect(_send_otp)
    def post(self):
        user_data = request.json
        email = user_data.get('Email')
        phone = user_data.get('PhoneNumber')
        country_code = user_data.get('CountryCode')
        return send_otp(email, phone, country_code)


@ns.route("/verify-otp")
class VerifyOTP(Resource):
    @ns.doc(params={"otp": "Enter the One Time Password send on Mobile"})
    def get(self):
        query = request.args
        return verification(query.get('otp'))
