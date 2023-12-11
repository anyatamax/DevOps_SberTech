# DevOps_SberTech
Lab3  
Было написано простое приложение на python в папке my_app/app.py  
#### Freestyle pipeline Jenkins
1) В первых шагах происходит сборка приложения через my_app/Dockerfile, там же прогоняются тесты и результат записывается в папку reports/  
2) SonarQube анализ идет в следующем шаге  
3) В конце создается allure report на основе тестов  
  
К джобе привязаны события (pull request and push) в github репозитории на ветку lab4 (для успешной работы надо прописать результат команды ngrok http 8080 в webhook на github)  
  
Для работы SonarQube он должен быть запущен через докер: docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest и через ngrok http 9000 получен адресс по которому можно обращаться к Sonar (актуальный адресс должен быть прописан в опициях к шагу с SonarQube)  

properties для SonarQube:  
sonar.projectBaseDir=my_app  
sonar.language=python  
sonar.host.url=https://da32-188-244-13-153.ngrok-free.app  
sonar.projectVersion=1.0  
sonar.sources=.  
sonar.verbose=true  
sonar.analysis.mode=publish  
sonar.projectKey=sonar_test_app  

#### Pipeline Jenkins  
Для работы в pipeline режиме необходимо прописать скрипт из файла Jenkins в pipeline джобе. Все остальные настройки остаются те же   

#### Как запустить Jenkins  
Запустить docker-compose up --build -d из главной директории. В этот момент в докер устанавливаются все необходимы зависимости и Jenkins будет доступен на http://localhost:8080/. Для входа: admin/93bfff3e8c0242e79731c2b36cefe85d  

#### Результаты отчета Allure и SonarQube:  
<img width="1726" alt="Screen Shot 2023-12-11 at 06 46 57" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/1c63a5be-3391-455a-9c98-0123e4acaf1d">  
<img width="1398" alt="Screen Shot 2023-12-11 at 06 55 36" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/f0f06130-058d-4de3-b568-448202b53db3">

