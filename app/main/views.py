"""
视图
"""

from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main

from .forms import NameForm
from .. import db
from ..models import User



@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user:
            session["know"] = True
        else:
            user = User(name=form.name.data)
            db.session.add(user)
            session["know"] = False
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template("index.html",
                           current_time=datetime.utcnow(),
                           form=form,
                           name=session.get('name'))


@main.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)