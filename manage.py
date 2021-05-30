from app import app
from app.config.config import APP_VERSION
from flask_script import Manager
manager = Manager(app)


@manager.option('-p', '--port', default=5001, help='Enter port name')
def run(**kwargs):
    app.run(host='0.0.0.0', port=kwargs['port'], debug=True)


@manager.command
def version():
    """ Version """
    return "Version: {0}".format(APP_VERSION)


if __name__ == '__main__':
    manager.run()
