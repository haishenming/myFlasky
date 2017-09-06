from datetime import datetime

from flask import Flask, render_template, session, url_for
from flask import request
from flask import make_response
from flask import redirect

from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template("index.html",
                           current_time=datetime.utcnow(),
                           form=form,
                           name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_page/404.html', error=e), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error_page/500.html', error=e), 500



if __name__ == '__main__':
    manager.run()
