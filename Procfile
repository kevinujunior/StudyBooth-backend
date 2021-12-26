release: python manage.py migrate
web: daphne studybooth.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=studybooth.settings -v2
