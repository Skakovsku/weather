FROM python:3.7-slim

RUN mkdir /app

COPY requirements.txt /app

RUN sudo python3 -m pip install --upgrade pip

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY weather/ /app

WORKDIR /app

CMD ["gunicorn", "weather.wsgi:application", "--bind", "0:8000" ]

RUN python3 manage.py collectstatic --no-input

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate
