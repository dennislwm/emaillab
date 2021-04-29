.PHONY: default install test verbose

default: test

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=./src pytest

verbose:
	PYTHONPATH=./src pytest -v -s
