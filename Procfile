release: python manage.py migrate
web: python manage.py collectstatic --noinput && gunicorn lbry.wsgi --log-file -