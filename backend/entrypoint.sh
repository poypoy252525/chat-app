#!/bin/sh
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker --workers 5 --bind 0.0.0.0:8000