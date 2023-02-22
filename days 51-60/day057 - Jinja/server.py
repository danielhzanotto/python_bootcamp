from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def init():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<name_user>')
def guess_gender(name_user):
    parameter = {'name': name_user}
    request_gender = requests.get(
        f'https://api.genderize.io/', params=parameter)
    gender_guessed = request_gender.json()['gender']
    request_age = requests.get(f'https://api.agify.io/', params=parameter)
    age_guessed = request_age.json()['age']
    return render_template('gender_generate.html', name=name_user.title(), gender=gender_guessed, age=age_guessed)


@app.route('/blog')
def generate_blog():
    response = requests.get('https://api.npoint.io/70ab90fa6b9423255a0b')
    response.raise_for_status()
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


@app.route('/blog/post/<post>')
def generate_post(post):
    response = requests.get('https://api.npoint.io/70ab90fa6b9423255a0b')
    response.raise_for_status()
    all_posts = response.json()
    post_selected = [p for p in all_posts if p['id'] == int(post)][0]
    return render_template('blog-post.html', posts=all_posts, post_selected=post_selected)


if __name__ == '__main__':
    app.run(debug=True)
