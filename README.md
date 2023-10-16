# DevOps_SberTech
MIPT course SberTech DevOps  
Приложение состоит из трех частей: само приложение на Flask, PostgreSQL и Nginx  
Из корня собрать и запустить приложение: docker-compose -f docker-compose.yml up -d --build  
Тогда по ссылке http://127.0.0.1:8000/ будет доступна стартовая страница приложения  
Далее создать бд можно через команду: docker-compose -f docker-compose.yml exec web python manage.py create_db  
И наполнить ее двумя строками: docker-compose -f docker-compose.yml exec web python manage.py seed_db 
Теперь по cсылке http://127.0.0.1:8000/users будут доступны все записи в бд

