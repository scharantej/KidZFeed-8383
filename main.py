
# main.py

from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

articles = [
    {
        "id": 1,
        "title": "Why the Sky is Blue",
        "content": "The sky is blue because of a phenomenon called Rayleigh scattering. This is when sunlight interacts with particles in the atmosphere, and the blue wavelengths of light are scattered more than the other colors."
    },
    {
        "id": 2,
        "title": "How do Plants Grow?",
        "content": "Plants grow by using sunlight, water, and carbon dioxide to create their own food through a process called photosynthesis. The sunlight is absorbed by chlorophyll in the plant's leaves, which then uses the energy to convert water and carbon dioxide into glucose, a type of sugar."
    },
    {
        "id": 3,
        "title": "What is the Solar System?",
        "content": "The solar system is a group of planets, moons, asteroids, and comets that orbit around the Sun. The Sun is a star, and it is the center of our solar system."
    }
]

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/article/<article_id>')
def article(article_id):
    article = [article for article in articles if article['id'] == int(article_id)][0]
    return render_template('article.html', article=article)

@app.route('/api/articles')
def api_articles():
    return jsonify(articles)

if __name__ == '__main__':
    app.run()
