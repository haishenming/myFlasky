from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello_world():
    response = make_response("<h1>make response</h1>")
    response.set_cookie('answer', '1')
    return response


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {name}!<h1>'.format(name=name)


if __name__ == '__main__':
    manager.run()
