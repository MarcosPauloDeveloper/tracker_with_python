from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password = db.Column(db.String(512), nullable=False)
    products = db.relationship('Product', backref='user')
    operations = db.relationship('Operations', backref='user')

    def __repr__(self):
        return self.name


db.create_all()
