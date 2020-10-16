FROM python:3.6.8

WORKDIR /opt/article_explorer

#RUN apt update
RUN apt-get update && apt-get install -y supervisor
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN pip install sparse-dot-topn==0.2.6

ENV C_FORCE_ROOT=1

COPY ./ /opt/article_explorer

CMD ["celery", "-A", "data_getter.celery:celery", "worker", "--beat", "--loglevel=INFO"]
