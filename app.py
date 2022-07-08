from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login.html'
login_manager.login_message_category = 'danger'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    admin = Admin(app, "Python Bank", template_mode="bootstrap4")
    db.init_app(app)
    login_manager.init_app(app)
    app.app_context().push()
    db.create_all()

    @app.route("/login")
    def login():
        return "login page"

    import admin as administrator
    administrator.init_app(admin)

    return app
