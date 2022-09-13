# Rishat
# Инструкция по разворачиванию приложения

#### Окружение проекта:
  * python 3.9
  * Django 4.1

#### Склонируйте репозиторий с помощью git:
```sh
git clone https://github.com/HowBoringAndSmall/Rishat
```

#### Перейдите в директорию проекта:
```sh
cd ./Rishat
```
#### Запустите команду docker:
```sh
docker-compose build
```
или
```sh
sudo docker-compose build
```
#### Создайте миграции приложения:
```sh
docker-compose run web python manage.py migrate
```
или
```sh
sudo docker-compose run web python manage.py migrate
```
#### Создайте суперпользователя:
```sh
docker-compose run web python manage.py createsuperuser
```
или
```sh
sudo docker-compose run web python manage.py createsuperuser
```
#### Заполните поля регистрации ( почта необязательна ):
```sh
Username (leave blank to use ...): 
Email address: 
Password: 
Password (again): 
Superuser created successfully. 
```

#### Запустите приложение (localhost: http://127.0.0.1:8000/):
```sh
docker-compose up
```
или
```sh
sudo docker-compose up
```
