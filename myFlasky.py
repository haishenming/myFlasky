from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import redirect

from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template("index.html")


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
