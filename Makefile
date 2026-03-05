.PHONY: test lint format hooks run

test:
	pytest

lint:
	flake8 .

format:
	black .

hooks:
	pre-commit run --all-files

run:
	python playground.py