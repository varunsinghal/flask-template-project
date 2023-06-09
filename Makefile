start:
	docker compose up -d 

stop:
	docker compose stop 

bash:
	docker compose exec flask bash

load_db:
	docker compose exec -T database bash ./load_db.sh 

clean:
	docker compose down --rmi local --volumes

install:
	docker compose exec -T flask pip install -r requirements.txt 

lint:
	docker compose exec -T flask black . --line-length 80
	docker compose exec -T flask isort .
	docker compose exec -T flask flake8 .

lint_check:
	docker compose exec -T flask flake8
	docker compose exec -T flask black . --line-length 80 --check
	docker compose exec -T flask isort . -c

serve:
	docker compose exec -T flask python main.py

test:
	docker-compose exec -T flask bash -c "python3 -m unittest discover tests -t . -v "

test_coverage:
	docker-compose exec -T flask bash -c "coverage run --source=. -m unittest discover tests -t ."
	docker-compose exec -T flask bash -c "coverage report -m --omit=tests/*"
