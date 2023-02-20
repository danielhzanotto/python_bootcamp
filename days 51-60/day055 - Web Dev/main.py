from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function


def make_italic(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function


@app.route('/')
def hello_world():
    return "<h1 style='text-align: center'>Hello, World</h1>"\
        "<p>This is a paragraph</p>"\
        '<iframe src="https://giphy.com/embed/ICOgUNjpvO0PC" width="480" height="359" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def say_bye():
    return 'bye'


@app.route('/username/<name>/<int:number>')
def greetings(name, number):
    return f'Hello {name}, take this number: {number}'


if __name__ == '__main__':
    app.run(debug=True)
