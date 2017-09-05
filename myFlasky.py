from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    user_agent = request.headers.get("User-Agent")
    return '<p>Your Browser is {}<p>'.format(user_agent)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {name}!<h1>'.format(name=name)


if __name__ == '__main__':
    app.run(debug=True)
