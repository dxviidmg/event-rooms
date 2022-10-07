release: python manage.py makemigrations
release: python manage.py migrate
web: daphne redspotAPI.asgi:application --port $PORT --bind 0.0.0.0