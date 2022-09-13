# Rishat
# Инструкция по разворачиванию приложения

#### Окружение проекта:
  * python 3.9
  * Django 4.1

#### Склонируйте репозиторий с помощью git:
```sh
git clone https://github.com/HowBoringAndSmall/Rishat
```
#### Создайте файл .env в Rishat/Rishat, где вы должны прописать:
STRIPE_SECRET_KEY=
STRIPE_PUBLIC_KEY=
SECRET_KEY=
последнее это ключ для django
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

#### Запустите приложение (ссылка: localhost:8000):
```sh
docker-compose up
```
или
```sh
sudo docker-compose up
```
#### Чтобы начать проверку вы должны создать item и зайти на него по ссылке. Например: http://localhost:8000/item/6/
#### В нём будет кнопка add to order и кнопка buy. Нажав на buy вы переходите на внешний stripe сервис. 
#### Нажам на add to order вы добавляете item в order(order для каждого ip пользователя разный) 
#### Дальше, чтобы проверить order вы можете перейти на ссылку http://localhost:8000/order/  В нём будет список товаров и их общая цена

