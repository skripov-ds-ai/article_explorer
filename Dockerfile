FROM python:3.6.8

WORKDIR /opt/article_explorer

RUN apt update
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ /opt/article_explorer

CMD ["gunicorn", "-b", "0.0.0.0:7777", "app:app"]
