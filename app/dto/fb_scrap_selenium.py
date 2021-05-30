from flask_restplus import Namespace, fields


ns = Namespace("Facebook", description="Facebook related data", path="/fb")


class FBSerializers:
    FBLoginData = ns.model('FbUser', {
        'Username': fields.String,
        'Password': fields.String
    })

