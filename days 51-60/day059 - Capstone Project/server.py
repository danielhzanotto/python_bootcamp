from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)


def get_year():
    return datetime.date.today().year


def get_posts():
    response = requests.get('https://api.npoint.io/70ab90fa6b9423255a0b')
    response.raise_for_status()
    return response.json()


@app.route('/')
def init():
    all_posts = get_posts()
    return render_template('index.html', posts=all_posts)


@app.route('/blog/<post>')
def generate_post(post):
    all_posts = get_posts()
    post_selected = [p for p in all_posts if p['id'] == int(post)][0]
    return render_template('blog-post.html', post_selected=post_selected)


@app.route('/about')
def about_me():
    return render_template('about-me.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
