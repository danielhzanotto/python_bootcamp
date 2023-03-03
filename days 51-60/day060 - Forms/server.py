from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def init():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def recieve_data():

    name = request.form['name']
    password = request.form['password']
    return render_template('login.html', name=name, password=password)


if __name__ == '__main__':
    app.run(debug=True)
