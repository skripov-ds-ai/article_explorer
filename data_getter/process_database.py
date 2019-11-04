from navigator.models import Article, Author, Category
from navigator import db
from data_getter.parse_categories import categories_to_long_name
from data_getter.download_preview import get_result, fill_template

# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker


# POSTGRES_USER = 'getter'
# POSTGRES_PW = 'qwerty1'
# POSTGRES_URL = "127.0.0.1:5432"
# POSTGRES_DB = "explorer"
#
#
# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
#         user=POSTGRES_USER,
#         pw=POSTGRES_PW,
#         url=POSTGRES_URL,
#         db=POSTGRES_DB
# )
#
# db = declarative_base()
# engine = sa.create_engine(DB_URL)
# db.metadata.bind = engine
# session = orm.scoped_session(orm.sessionmaker())(bind=engine)
# db.session = session

# db = SQLAlchemy()


def transaction_single_article(datum):
    authors = datum.get('authors')
    for author_name in authors:
        author = Author(name=author_name)
        try:
            db.session.add(author)
            db.session.commit()
        except:
            # print('TROUBLE authors')
            db.session.rollback()

    authors_to_article = []
    for author_name in authors:
        author = Author.query.filter(
            Author.name == author_name
        ).first()
        if author is not None:
            authors_to_article.append(author)
        # print(authors_to_article)

    categories = datum.get('categories')
    for category_name in categories:
        if category_name in categories_to_long_name:
            long_name = categories_to_long_name[category_name]
        else:
            long_name = category_name
        category = Category(
            small_name=category_name,
            name=long_name,
        )
        try:
            db.session.add(category)
            db.session.commit()
        except:
            # print('TROUBLE categories')
            db.session.rollback()
        # db.session.merge(category)
    # db.session.commit()

    categories_to_article = []
    for category_name in categories:
        category = Category.query.filter(
            Category.small_name == category_name
        ).first()
        if category is not None:
            categories_to_article.append(category)
        # print(categories_to_article)

    article = Article(
        title=datum.get('title'),
        summary=datum.get('summary'),
        url=datum.get('url'),
        published=datum.get('published'),
        updated=datum.get('updated'),
        categories=categories_to_article,
        authors=authors_to_article,
    )
    try:
        db.session.add(article)
        db.session.commit()
    except:
        # print('TROUBLE article')
        db.session.rollback()


# db.session.rollback()
data = []
for cat in [
    'math.CT'
    'stat.TH',
    'stat.ML',
    'math.QA',
    'math.MP',
    'eess.IV',
    'math.CA',
    'math.FA'
]:
    print(fill_template(cat, 700, 100))
    data1 = get_result(cat, 700, 100)
    data.extend(data1)

from tqdm import tqdm
for datum in tqdm(data):
    transaction_single_article(datum)






