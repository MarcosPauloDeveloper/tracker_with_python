from models.user import User
from models.product import Product
from flask_admin.contrib.sqla import ModelView
from wtforms.fields import PasswordField, EmailField
from werkzeug.security import generate_password_hash
from app import db


class UserView(ModelView):
    edit_modal = True
    create_modal = True
    form_edit_rules = {'name', 'email'}
    column_searchable_list = ['email']
    form_extra_fields = {
        "email": EmailField("Email"),
        "password": PasswordField("Password")
    }
    column_filters = ['name']
    column_exclude_list = ('password')

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(form.password.data)


def init_app(admin):
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Product, db.session))
