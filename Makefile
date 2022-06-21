migrate:
	python3.8 manage.py migrate

run:
	python3.8 manage.py runserver

test:
	python3.8 manage.py test

up:
	docker-compose up

down:
	docker-compose down -v

build:
	docker-compose build

test:
	python3.8 manage.py test -v 2
