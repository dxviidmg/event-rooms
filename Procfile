release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn event_rooms.wsgi --log-file -