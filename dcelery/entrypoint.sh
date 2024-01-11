#!/bin/sh

echo "Apply DB Migrations"
python manage.py migrate

exec "$@"
