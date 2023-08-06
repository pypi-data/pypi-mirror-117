init:
	pip install --upgrade pip-tools pip setuptools
	pip install --editable .
	pip install --upgrade -r requirements/main.txt  -r requirements/dev.txt

update-deps:
	pip install --upgrade pip-tools pip setuptools
	pip-compile --upgrade --build-isolation --generate-hashes --output-file \
		requirements/main.txt requirements/main.in
	pip-compile --upgrade --build-isolation --generate-hashes --output-file \
		requirements/dev.txt requirements/dev.in

update: update-deps init

up-dev:
	docker compose up --build --force-recreate --detach

down-dev:
	docker compose down

follow-fastapi:
	docker compose logs fastapi -f

fastapi-docker:
	./docker-build.sh polyneme/nmdc-runtime-fastapi nmdc_runtime/fastapi.Dockerfile

dagster-docker:
	./docker-build.sh polyneme/nmdc-runtime-dagster nmdc_runtime/dagster.Dockerfile

publish:
	invoke publish

docs:
	# assumes `make up-dev`.
	# nvm use 14
	redoc-cli bundle http://0.0.0.0:8000/openapi.json -o docs/design/redoc-static.html

.PHONY: init update-deps update up-dev down-dev follow-fastapi \
	fastapi-docker dagster-docker publish docs