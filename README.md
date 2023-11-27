## Первая часть 
###  Сборка приложения на "чистом" сборщике 
Для сборки приложения выполнить команду:  
cd task1  
ansible-playbook --connection=local --inventory 127.0.0.1, main.yml  
Далее по адресу http://127.0.0.1:8000/ - выводится Hello World  
Под капотом клонируется из главной ветки простое приложение на flask, которое выводит Hello World 

## Вторая часть 
###  Деплой  ваше приложение с shell скриптом его запуск  
Перейти в нужную папку: cd task2  
Для сборки докера выполнить:  
docker build -t debian-ssh -f start_docker .  
docker run -d -i -p 2200:22 -p 8002:8000 --name debian-ssh -v /var/run/docker.sock:/var/run/docker.sock debian-ssh  
Далее запустить ansible-playbook:  
ansible-playbook -i inventory.yml start.yml  
Далее по адресу http://127.0.0.1:8000/ - выводится Hello World  
Под капотом клонируется из главной ветки простое приложение на flask, которое выводит Hello World 