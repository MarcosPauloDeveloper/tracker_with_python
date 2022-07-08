from models.user import User
from flask import redirect
from models.product import Product
from models.user_operations import Operations
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink, SubMenuCategory, MenuCategory, BaseMenu
from wtforms.fields import PasswordField, EmailField
from flask_login import current_user
from werkzeug.security import generate_password_hash
from app import db


class UserView(ModelView):
    edit_modal = True
    create_modal = True
    form_edit_rules = {'name', 'email'}
    column_searchable_list = ['email', 'name']
    form_extra_fields = {
        "email": EmailField("Email"),
        "password": PasswordField("Password")
    }
    column_filters = ['name']
    column_exclude_list = 'password'
    can_delete = False
    can_view_details = True
    column_details_exclude_list = 'password'
    column_sortable_list = ['name']
    column_descriptions = {
        'email': 'email do usuário da sessão atual.'
    }

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.password = generate_password_hash(form.password.data)

    def inaccessible_callback(self, name, **kwargs):
        return redirect("/login")


def init_app(admin):
    admin.add_view(UserView(User, db.session, category='Perfil'))
    admin.add_view(ModelView(Product, db.session, category='Pagamentos'))
    admin.add_link(MenuLink(name='Logout', url='/logout'))

