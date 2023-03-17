setup:
	virtualenv env

start:
	source env/bin/activate

build:
	docker compose up --build

up:
	docker compose up

down:
	docker compose down

restart:
	docker compose restart

rebuild:
	docker compose up --build
