#!/bin/sh

# if any command fails, everything fails for safety
set -e

python manage.py wait_for_db
# put all static files in one directory for reverse proxy
python manage.py collectstatic --noinput
python manage.py migrate

# runs wsgi service, 4 workers (can change), set daemon as master, enable multi-threading, run app/wsgi.py
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
