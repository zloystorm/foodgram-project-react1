Python
Django
Docker
postgresql
nginx
gunicorn

cd foodgram-project-react/backend/
docker-compose up -d
docker-compose exec backend python manage.py migrate --noinput
- docker-compose exec backend python manage.py collectstatic --no-input && docker-compose exec backend python manage.py createsuperuser
