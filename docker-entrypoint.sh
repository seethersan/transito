#!/bin/bash
sleep 10
python /home/app/webapp/manage.py migrate
python /home/app/webapp/manage.py runserver 0.0.0.0:8000
exec "$@"