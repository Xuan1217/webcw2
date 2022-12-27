from flask_script import Manager
from app import app

manager = Manager(app)


@manager.command
def hello():
    # just a test command
    print("OK")
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, threaded=True)