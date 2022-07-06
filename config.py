import os

class Config:
    FLASK_ADMIN_SWATCH = "flatly"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:4132@localhost/tracker'
    SECRET_KEY = "SECRET"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["DATABASE_TRACK_MODIFICATIONS"]