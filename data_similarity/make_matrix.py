from sklearn.feature_extraction.text import HashingVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sparse_dot_topn import awesome_cossim_topn

from navigator.models import Article, Author, Category
from navigator import db

import numpy as np
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import word_tokenize


def get_csr_ntop_idx_data(csr_row, ntop):
    """
    Get list (row index, score) of the n top matches
    """
    nnz = csr_row.getnnz()
    if nnz == 0:
        return None
    elif nnz <= ntop:
        result = zip(csr_row.indices, csr_row.data)
    else:
        arg_idx = np.argpartition(csr_row.data, -ntop)[-ntop:]
        result = zip(csr_row.indices[arg_idx], csr_row.data[arg_idx])

    return sorted(result, key=lambda x: -x[1])


articles_id_text = Article.query.with_entities(Article.id, Article.title, Article.summary).all()

from pprint import pprint
pprint(articles_id_text)

ids = [x[0] for x in articles_id_text]
titles = [x[1] for x in articles_id_text]
texts = [x[2] for x in articles_id_text]

tmp = [x[0] + " " + x[1] for x in zip(titles, texts)]

stemmer = WordNetLemmatizer()


def text_preprocess(x):
    tmp = word_tokenize(x)
    tmp = list(map(lambda w: stemmer.lemmatize(w), tmp))
    return ' '.join(tmp)


tmp = list(map(text_preprocess, tmp))


vect = HashingVectorizer(analyzer='char', ngram_range=(1, 4))
tfidf = TfidfTransformer(
    # sublinear_tf=True
)
features = Pipeline(
    steps=[
        ('vect', vect),
        ('tfidf', tfidf)
    ]
)

tfidf_matrix = features.fit_transform(tmp)

cosine_matrix = awesome_cossim_topn(
    tfidf_matrix,
    tfidf_matrix.transpose(),
  # vals.size,
    10,
    0.1,
    use_threads=True,
    n_jobs=3
)

pprint(cosine_matrix)

pprint(get_csr_ntop_idx_data(cosine_matrix[2], 5))

pprint(Article.query.get(3).summary)
pprint(Article.query.get(11).summary)



