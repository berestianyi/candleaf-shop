FROM python:3.10.14-alpine3.19

LABEL authors="ivan.berestianyi"

WORKDIR /usr/src/candleaf

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r /usr/src/requirements.txt
RUN apk add --update nodejs npm

COPY . /usr/src/candleaf

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]