# Скородум Генератор. Backend

## Первичная настройка

1. Получите пакет redist, который содержит в себе
    - python-install.exe (v3.12)
2. Откройте файл `0ИНСТРУКЦИЯ.txt` в папке `УПРАВЛЕНИЕ`
3. Cледуйте инструкции

## Запуск

Запуск выполняется согласно инструкции, а также открыв консоль в этой папке
(Windows: Shift+ПКМ > Открыть консоль/powershell)

- `python manage.py runserver` — запускает сервер на текущей машине (localhost)
- `python manage.py runserver 192.168.33.33:8888` — запускает сервер на IP 192.168.33.33 c портом 8888 (прим. wifi)
- `python manage.py makemigrations` — при редактировании модели создает миграции для БД
- `python manage.py migrate` — мигрирует изменения модели в БД
- `python manage.py createsuperuser` — создает админа (для доступа к http://serverip/admin)

## Особенности деплоя под linux

Необходимо установить пакет gunicorn и запустить его, настроив `gunicorn.service` и `gunicorn.socket`.

### Пример gunicorn.service
```
# /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=unimon
Group=www-data
WorkingDirectory=/var/www/Skorodum
ExecStart=/var/www/Skorodum/venv/bin/gunicorn --chdir /var/www/Skorodum/skorodum --access-logfile - --workers 1  --bind unix:/run/gunicorn.sock skorodum.wsgi:application

[Install]
WantedBy=multi-user.target

```
### Пример gunicorn.socket
```
# /etc/systemd/system/gunicorn.socket

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```
### Пример конфигурации NGINX
```
# /etc/nginx/sites-available/skorodum-back.conf

server {
    server_name YOUR_SERVER_DOMAIN;
    #auth_basic "Protected API";
    #auth_basic_user_file /etc/nginx/.htpasswd;
    location = /favicon.ico { access_log off; log_not_found off; }
    location / {
	include proxy_params;
	proxy_pass http://unix:/run/gunicorn.sock;
    }


    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/YOUR_SERVER_DOMAIN/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/YOUR_SERVER_DOMAIN/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}server {
    if ($host = YOUR_SERVER_DOMAIN) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    server_name YOUR_SERVER_DOMAIN;
    return 404; # managed by Certbot


}
```
>Также не забудьте перед этим установить зависимости, виртуальную среду, папку run и все сопутствующие

## Список эндпоинтов

Можно получить перейдя на любую незадекларированную страницу, например `/`
