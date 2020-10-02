init:
	pip install -e .
	pip install -r requirements.txt

test:
	pytest

.PHONY: init test
