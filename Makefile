up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose down
	docker compose up -d

logs:
	docker compose logs -f

ps:
	docker compose ps
	
test:
	pytest tests/

lint:
	flake8 scripts/
	pylint scripts/

docs:
	rm -rf docs
	python3 -m pdoc --output-dir docs scripts


