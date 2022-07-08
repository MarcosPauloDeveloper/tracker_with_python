from app import db
from flask_login import UserMixin


class Operations(db.Model, UserMixin):
    __tablename__ = 'user_operations'

    id = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Float, nullable=False)
    chave_pix_cpf = db.Column(db.Boolean, nullable=False)
    chave_pix_email = db.Column(db.Boolean, nullable=False)
    limite = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __repr__(self):
        return self.id


db.create_all()
