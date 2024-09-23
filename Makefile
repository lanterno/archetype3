build:
	docker compose build
up:
	docker compose up
makemigrations:
	docker compose run --rm api python manage.py makemigrations
migrate:
	docker compose run --rm api python manage.py migrate
restart-api:
	docker compose restart api
pytest: export API_ENV_FILE := config/test.env
pytest:
	docker compose run --rm api python -m pytest
shell:
	docker compose run --rm api python manage.py shell_plus
bash:
	docker compose run --rm api bash

clean:
	poetry run black .
	poetry run isort .