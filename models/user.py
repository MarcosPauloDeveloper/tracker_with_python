from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password = db.Column(db.String(512), nullable=False)
    products = db.relationship('Product', backref='user')

    def __repr__(self):
        return self.name


db.create_all()
