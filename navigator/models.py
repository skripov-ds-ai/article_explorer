from datetime import datetime
from navigator import db


category_2_article = db.Table(
    'cat2art',
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')),
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id'))
)

author_2_article = db.Table(
    'auth2art',
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id')),
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id'))
)


# TODO: make good primary key!!!
class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text(), unique=True)
    title = db.Column(db.String(200), index=True)
    summary = db.Column(db.Text(), index=True)
    published = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    categories = db.relationship("Category", secondary=category_2_article)
    authors = db.relationship("Author", secondary=author_2_article)

    def __repr__(self):
        return '<Article {}>'.format(self.title)


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    small_name = db.Column(db.String(50), index=True, unique=True)
    name = db.Column(db.String(150), index=True)

    def __repr__(self):
        return '<Category {}>'.format(self.name)


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True, unique=True)

    def __repr__(self):
        return '<Author {}>'.format(self.name)





