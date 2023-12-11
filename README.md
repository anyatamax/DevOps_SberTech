# DevOps_SberTech
Lab3  
Было написано простое приложение на python в папке my_app/app.py  
#### Freestyle pipeline Jenkins
1) В первых шагах происходит сборка приложения через my_app/Dockerfile, там же прогоняются тесты и результат записывается в папку reports/
<img width="1728" alt="Screen Shot 2023-12-10 at 18 43 39" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/4782c089-e525-4e66-b8b1-e1bed06b4394">
<img width="1723" alt="Screen Shot 2023-12-10 at 18 43 47" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/1746bd60-dc4e-44f8-b16d-925eb8234447">
<img width="1726" alt="Screen Shot 2023-12-10 at 18 43 55" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/02e821d5-3a13-4079-8d8f-47f043c25966">
<img width="1728" alt="Screen Shot 2023-12-10 at 18 44 02" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/2a425409-a366-4165-8088-8e5491c4f774">
<img width="1720" alt="Screen Shot 2023-12-10 at 18 44 12" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/3117259f-803c-461f-b7fa-a652f46a0113">  
2) SonarQube анализ идет в следующем шаге
<img width="1727" alt="Screen Shot 2023-12-10 at 18 44 23" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/1044a89f-7efa-478a-b63e-021067bee179">  
3) В конце создается allure report на основе тестов
<img width="1719" alt="Screen Shot 2023-12-10 at 18 44 30" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/91618c15-90da-489e-8a85-e155cd745a4c">  

<img width="1400" alt="Screen Shot 2023-12-11 at 07 01 23" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/1d89208b-5a0e-4842-95a6-21a406ee00cb">  

К джобе привязаны события (pull request and push) в github репозитории на ветку lab4 (для успешной работы надо прописать результат команды ngrok http 8080 в webhook на github)  
  
Для работы SonarQube он должен быть запущен через докер: docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest и через ngrok http 9000 получен адрес по которому можно обращаться к Sonar (актуальный адресс должен быть прописан в опициях к шагу с SonarQube)  

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
<img width="1726" alt="Screen Shot 2023-12-11 at 06 46 57" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/840c5fe0-226d-40c5-ad68-f29a93ef4e93">
<img width="1397" alt="Screen Shot 2023-12-11 at 06 57 24" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/60cede3c-17f8-403e-ac5a-0111f0d61149">


#### Как запустить Jenkins  
Запустить docker-compose up --build -d из главной директории. В этот момент в докер устанавливаются все необходимые зависимости и Jenkins будет доступен на http://localhost:8080/. Для входа: admin/93bfff3e8c0242e79731c2b36cefe85d  

#### Результаты отчета Allure и SonarQube:  
<img width="1726" alt="Screen Shot 2023-12-11 at 06 46 57" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/1c63a5be-3391-455a-9c98-0123e4acaf1d">  
<img width="1398" alt="Screen Shot 2023-12-11 at 06 55 36" src="https://github.com/anyatamax/DevOps_SberTech/assets/71087982/f0f06130-058d-4de3-b568-448202b53db3">

