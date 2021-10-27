migrations:
	@docker exec -it -w /code cardealer python manage.py makemigrations

migrate:
	@docker exec -it -w /code cardealer python manage.py migrate

app:
	@mkdir -p src/apps/$(name)
	@docker exec -it -w /code cardealer python manage.py startapp $(name) src/apps/$(name)

start_compose:
	@docker-compose up

test_user:
	@docker exec -it -w /code cardealer python manage.py createsuperuser
