## Запуск сервера

``` python manage.py runserver ``` 

можно указать любой свободный порт + сделать без автоперезагрузки

``` python manage.py runserver 0.0.0.0:8000 --noreload ```

Остановить сервак ``` ctrl + C ```

## Миграции

``` python manage.py makemigrations``` // создать миграции

``` python manage.py migrate ``` // применить миграции