# from navigator import db
import scipy.sparse
import numpy as np
from navigator.routes import Article
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

articles = Article.query.order_by(Article.updated.desc()).all()
article_ids = [a.id for a in articles]
article_summary = [a.summary for a in articles]
# print(articles)
tfidf = TfidfVectorizer(ngram_range=(1, 3)).fit(article_summary)
articles_tfidf = tfidf.transform(article_summary)
sim = cosine_similarity(articles_tfidf, dense_output=False)


# print(sim.shape)
# sim.eliminate_zeros()
#
# arr = sim[0].toarray().squeeze()
# print(arr.shape, arr[0].shape)
# print(len(arr))
#
# idx = np.argsort(arr)[-6:-1]
# print(len(arr))
# print(arr[idx])
# print(arr[idx].shape)
# print()
# print(type(sim))

scipy.sparse.save_npz("../cosine_sim_articles.npz", sim)
