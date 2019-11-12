FROM python:3.7-buster

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN echo 'en_US ISO-8859-1 ' >> /etc/locale.gen 
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen 
RUN echo 'fr_FR.UTF-8 UTF-8' >> /etc/locale.gen 
RUN echo 'fr_FR ISO-8859-1' >> /etc/locale.gen
RUN locale-gen

RUN pip install argparse mysql-connector-python beautifulsoup4 requests

COPY . /usr/src/themoviepredictor

WORKDIR /usr/src/themoviepredictor

CMD python app.py movies import --api omdb --imdbId tt3896198