from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

all_books = []

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collections.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


with app.app_context():
    class Books(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.String(250), nullable=False)

        def __repr__(self):
            return '<books %r>' % self.title


class LoginForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    rating = SelectField(label='Rating', validators=[DataRequired()], choices=[
                         (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    submit = SubmitField(label='Add Book')


@app.route('/')
def home():
    print(len(all_books))
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        new_book = Books(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html', form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
