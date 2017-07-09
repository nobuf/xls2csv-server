FROM debian:jessie

RUN apt-get update
RUN apt-get install -y libreoffice
RUN apt-get install -y curl
RUN apt-get install -y python python-pip

RUN pip install xlsx2csv
RUN pip install Flask

COPY . /app
ENV FLASK_APP /app/app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]