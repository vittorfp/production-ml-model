FROM python:3.6 AS BUILD

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/

ONBUILD COPY app/requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r app/requirements.txt

FROM BUILD

ADD . /usr/src/
ENTRYPOINT python app.py
EXPOSE 5000