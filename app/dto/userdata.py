from flask_restplus import Namespace, fields


ns = Namespace("User", description="User related operations", path="/user")


class UserDataSerializers:
    UserData = ns.model('User', {
        'Email': fields.String,
        'PhoneNumber': fields.String,
        'CountryCode': fields.String
    })
    UserCredentials = ns.model('UserCredentials', {
        'Email': fields.String,
        'UserName': fields.String,
        'PassWord': fields.String
    })
    UserRegistration = ns.model('UserRegistration', {
        'Email': fields.String,
        'PhoneNumber': fields.String,
        'UserName': fields.String,
        'PassWord': fields.String,
        'FirstName': fields.String,
        'LastName': fields.String
    })
