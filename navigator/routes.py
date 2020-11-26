import numpy as np
import scipy.sparse
from flask import render_template
from sqlalchemy.sql.expression import func


from navigator import app
from navigator.models import Article

SIMILARITY_FILE = 'cosine_sim_articles.npz'

sim = scipy.sparse.load_npz(SIMILARITY_FILE)


@app.route('/', defaults={'page': 1})
@app.route('/<int:page>')
def index(page):
    per_page = 10
    error_out = False
    articles = Article.query.order_by(
        Article.updated.desc()
    ).paginate(
        page=page,
        per_page=per_page,
        error_out=error_out
    )
    return render_template('index.html', articles=articles)


@app.route('/article/<int:id>')
def article_page(id):
    article = Article.query.get(id)
    idxs = []
    if id < max(sim.shape):
        arr = sim[id].toarray().squeeze()
        idxs = [int(i) for i in np.argsort(arr)[1:6]]

    similar = []
    try:
        if len(idxs) > 0:
            similar = Article.query.filter(Article.id.in_(idxs))
            similar = similar.limit(5)
    except:
        similar = []

    return render_template('article.html', article=article, similar=similar)


