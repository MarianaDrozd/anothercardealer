# anothercardealer
Django project CarDealer with Docker-Compose usage
# Setup

#### Create local env file

Just run `make test_env`


#### Build containers

#### Before running project 

- Create local env file
- Build containers `docker-compose build`
- Run project

####   Run project   

`docker-compose up`


#### When project is running 

- Apply db migrations `make migrations`
- Create superuser `make test_user`. After that you will be able to login into Admin
- Enjoy! :)

#### Create new app 

`make app name=<app_name>`

#### Project description  

This is my simple project that I was started while studying at CURSOR.EDUCATION.
- You are able to see Django Admin and create some data in DB
- Now you can see cars, dealers, orders there

#### All commands you can find in `Makefile`

Just type `make {command}` in your terminal.
You don't need to remember sooo much commands.
Easy! :)
