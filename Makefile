VENV_PATH=".venv"

init:
	python3 -m venv ${VENV_PATH}
	${VENV_PATH}/bin/pip install -U pip setuptools
	${VENV_PATH}/bin/pip install poetry

pretty:
	${VENV_PATH}/bin/ruff format .
	
lint:
	${VENV_PATH}/bin/ruff check .

plint: pretty lint

build: 
	docker-compose build

run_tests:
	echo "a"
	${VENV_PATH}/bin/pytest .

prepare_local_run:
	docker-compose up postgres -d 
	docker-compose run migration_runner

local_run:
	docker-compose up -d