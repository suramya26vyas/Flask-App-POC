from flask_restplus import Namespace, fields


ns = Namespace("OTP", description="One Time Password related data", path="/otp")


class OTPSerializers:
    UserData = ns.model('User', {
        'Email': fields.String,
        'PhoneNumber': fields.String,
        'CountryCode': fields.String
    })

