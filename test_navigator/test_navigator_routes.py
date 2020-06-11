import json

from flask import Blueprint, render_template, request, url_for
from flask_api.status import HTTP_200_OK
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from test_navigator.test_navigator_utils import get_users, add_user, get_users_remote

bp = Blueprint('gui', __name__)


class AddUserForm(FlaskForm):
    user_name = StringField('Имя пользователя:',
                            validators=[DataRequired("Пожалуйста, введите корректное имя")])
    submit = SubmitField('Добавить')


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = AddUserForm()
        # response = get_users()
        response = get_users_remote()

        if response.status_code == HTTP_200_OK:
            users = json.loads(response.content)
            if users is None:
                return render_template('index.html', form=form)

            return render_template('index.html',
                                   users=users['users'],
                                   form=form)
        else:
            return render_template('index.html', form=form)

    elif request.method == 'POST':
        user_name = request.form["user_name"]
        add_user(user_name)
        return redirect(url_for('gui.index'))
