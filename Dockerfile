FROM python:3.9

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -U -r requirements.txt

COPY . .

CMD gunicorn justfound.wsgi:application --bind 0.0.0.0:8000

