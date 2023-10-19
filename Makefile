.PHONY: deploy dev

requirements.txt: pyproject.toml
	poetry export -f $@ -o $@ --without-hashes


deploy: requirements.txt
	space push

dev:
	poetry run uvicorn app.main:app
