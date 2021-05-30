import os

basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

APP_VERSION = 0.1

class Config:
    """Set Flask configuration vars from .env file."""

    # General
    # TESTING = environ.get('TESTING')
    # FLASK_DEBUG = environ.get('FLASK_DEBUG')
    # SECRET_KEY = environ.get('SECRET_KEY')
    SECRET_KEY = os.getenv("SECRET_KEY",
                           "J_a7HWO9LeQZHRsaOHeoE_JvDLxo3dQFrON9UagxWk0=")
    DEBUG = False
    # Database
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\suramya.vyas\\PycharmProjects\\TestTwilio\\college.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, "college.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


ENC_DEC_KEY = Config.SECRET_KEY