init:
	pip install -r requirements.txt

test:
	python -m pytest

.PHONY: init test
