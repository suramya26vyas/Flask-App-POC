from flask_restplus import Namespace, fields


ns = Namespace("Web-Scrap", description="Display Web Scrapped data", path="/scrap")


class WebScrapSerializers:
    WebScrapData = ns.model('WebScrap', {
        'Job': fields.String,
        'Country': fields.String,
    })

    WebScrapLoginData = ns.model('WebScrapLogin', {
        'Email': fields.String,
        'Password': fields.String,
    })