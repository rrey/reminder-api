FROM python:2.7-slim

RUN mkdir -p /etc/reminder_api
RUN pip install gunicorn json-logging-py

COPY requirements.txt /etc/reminder_api/requirements.txt
RUN pip install -r /etc/reminder_api/requirements.txt

COPY docker/logging.conf /etc/reminder_api/logging.conf
COPY docker/gunicorn.conf /etc/reminder_api/gunicorn.conf
COPY reminder_api /opt/reminder_api

RUN cd /opt/reminder_api;                      \
    python manage.py makemigrations project;   \
    python manage.py makemigrations reminder;  \
    python manage.py makemigrations inventory; \
    python manage.py migrate

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--chdir", "/opt/reminder_api",  "--config", "/etc/reminder_api/gunicorn.conf", "--log-config", "/etc/reminder_api/logging.conf",  "reminder_api.wsgi:application"]
