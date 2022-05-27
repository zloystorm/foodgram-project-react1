Автор: 

    Салтанов Д.С.
    Студент яндекс практикума.

Технологии:

    Python
    Django
    Docker
    postgresql
    nginx
    gunicorn

Для запуска приложения нужно выполнить следующее:

Клонируйте репозиторий командой:
git clone https://github.com/zloystorm/foodgram-project-react.git

Перейдите в каталог командой:
cd foodgram-project-react/backend/

Выполните команду для запуска контейнера:
docker-compose up -d

Выполните миграции:
docker-compose exec backend python manage.py migrate --noinput

Команда для сбора статики:
- docker-compose exec backend python manage.py collectstatic --no-input

Команда для создания суперпользователя:
docker-compose exec backend python manage.py createsuperuser

Приложение можно найти по следующему ip: 84.252.138.97