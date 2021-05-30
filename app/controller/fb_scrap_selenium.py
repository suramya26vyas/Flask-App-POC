from flask_restplus import Resource
from ..services.fb_scrap import fb_login_selenium
from ..dto.fb_scrap_selenium import FBSerializers, ns
from flask import request

_FBLogin = FBSerializers.FBLoginData


@ns.route("/fb")
class WebScrap(Resource):
    @ns.expect(_FBLogin)
    def post(self):
        required_job_data = request.json
        return fb_login_selenium(required_job_data)
