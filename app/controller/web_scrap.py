from flask_restplus import Resource, Namespace
from ..services.web_scrap import get_webscrap_data, get_names_of_all_git_projects
from ..dto.web_scrap import WebScrapSerializers, ns
from flask import request

_WebScrapData = WebScrapSerializers.WebScrapData
_WebScrapLoginData = WebScrapSerializers.WebScrapLoginData


@ns.route("/web-scrap")
class WebScrap(Resource):
    @ns.expect(_WebScrapData)
    def post(self):
        required_job_data = request.json
        return {"JobsData": get_webscrap_data(required_job_data)}


@ns.route("/web-scrap-login")
class WebScrapSelenium(Resource):
    @ns.expect(_WebScrapLoginData)
    def post(self):
        required_job_data = request.json
        return {"JobsData": get_names_of_all_git_projects(required_job_data)}