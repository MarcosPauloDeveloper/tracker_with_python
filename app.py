from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    admin = Admin(app, "Tracker", template_mode="bootstrap3")
    db.init_app(app)

    app.app_context().push()
    db.create_all()

    import admin as administrator
    administrator.init_app(admin)

    return app
