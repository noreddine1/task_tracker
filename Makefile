run:
	@python main.py

test:
	@pytest

clean:
	@rm -rf __pycache__ *.pyc .pytest_cache

.PHONY: run test clean