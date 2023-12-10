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
