#!/bin/sh
exec $( rm db.sqlite3 && ./manage.py migrate && ./manage.py runserver )
