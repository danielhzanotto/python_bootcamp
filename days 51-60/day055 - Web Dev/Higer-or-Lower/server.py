from flask import Flask
import random

app = Flask(__name__)

generated_number = random.randint(0, 9)


@app.route('/')
def hello_world():
    return "<h1>Guess the number between 0 and 9</h1>"\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="gif" width="300">'


@app.route('/<int:number>')
def guess_number(number):
    print(generated_number)
    if number > 9:
        return "<h1 style=color: red>Too Low, Try Again!</h1>"\
            '<img src=" https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="gif" width="300">'
    elif number < generated_number:
        return "<h1 style=color: purple>Too High, Try Again!</h1>"\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="gif" width="300">'
    elif number > generated_number:
        return "<h1 style=color: green>You Found Me!</h1>"\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="gif" width="300">'
    else:
        return f'Correct! The number is {generated_number}'


if __name__ == '__main__':
    app.run(debug=True)
