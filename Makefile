init:
	pip install -r requirements.txt

freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt

test:
	pytest

.PHONY: init test freeze
