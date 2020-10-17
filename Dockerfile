FROM python:3.6.8

WORKDIR /opt/article_explorer

RUN apt update
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install sparse-dot-topn==0.2.6

COPY ./ /opt/article_explorer

#CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
COPY entrypoint.sh .
RUN chmod u+x ./entrypoint.sh
#ENTRYPOINT ["./entrypoint.sh"]
CMD ["/bin/bash", "./entrypoint.sh"]
