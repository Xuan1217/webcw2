import logging
from logging.config import dictConfig
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_URI

dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {  # Style
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",  # Console output
                "level": "DEBUG",
                "formatter": "default",
            },
            "log_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "default",
                "filename": "flask.log",    # logger location
                "maxBytes": 20*1024*1024,   # logger size
                "backupCount": 10,
                "encoding": "utf8",
            },

        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console", "log_file"],
        },
    }
)

app = Flask(__name__)       # init the flask by app

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI            # this is database's url (the whole url can find in config.py)
app.config['SECRET_KEY'] = '654321'                       # the secret key
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import views
