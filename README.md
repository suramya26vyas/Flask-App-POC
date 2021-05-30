# Flask App POC

If we are using only Flask and Api from flask_restplus
 1) First Create and app through Flask
 2) Add app object to Api and create an object api
 3)	Use api.route to call the endpoints

 
If we are using only Flask, Blueprint and  Api from flask_restplus

 1) First Create and app through Flask
 2) Create a Blueprint Object with a name say test_blueprint
 3)	Add that object in the app object through the method register_blueprint
 4) Add app object to Api and create an object api
 5)	Use test_blueprint.route to call the endpoints

If we are using only Flask, Blueprint and  Api, Namespace from flask_restplus
 1) First Create and app through Flask
 2) Create a Blueprint Object with a name say test_blueprint
 3)	Add that object in the app object through the method register_blueprint
 4) Add app object to Api and create an object api
 5)	In the controller file create a Namespace object
 6)	Add Namespace to the api object
 
 
Creating DB Config.
There are a few variables here which are specific to Flask-SQLAlchemy:
In config/config.py

SQLALCHEMY_DATABASE_URI: the connection string we need to connect to our database. This follows the standard convention:
 [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
 
SQLALCHEMY_ECHO: When set to 'True', Flask-SQLAlchemy will log all database activity to Python's stderr for debugging purposes.

SQLALCHEMY_TRACK_MODIFICATIONS: Honestly, I just always set this to 'False,'
 otherwise an obnoxious warning appears every time you run your app reminding you that this option takes a lot of system resources.