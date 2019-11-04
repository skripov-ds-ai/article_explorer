from flask import render_template
from sqlalchemy.sql.expression import func

from navigator import app
from navigator.models import Article


@app.route('/')
def index():
    articles = Article.query.order_by(Article.updated.desc())#.limit(30)#func.random()).limit(10).all()
    return render_template('index.html', articles=articles)


@app.route('/article/<int:id>')
def article_page(id):
    article = Article.query.get(id)
    similar = []
    similar = Article.query.order_by(func.random()).limit(5)

    return render_template('article.html', article=article, similar=similar)


