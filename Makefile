VENV     = $(CURDIR)/env
PIP      = $(VENV)/bin/pip

test: | env
	$(VENV)/bin/coverage run --rcfile=coverage.cfg -m unittest discover ./tests
	$(VENV)/bin/coverage report --rcfile=coverage.cfg
	$(VENV)/bin/coverage html --rcfile=coverage.cfg
	touch htmlcov

test-watch: | dev-env
	$(VENV)/bin/sniffer

shell: | dev-env
	$(VENV)/bin/ipython

clean:
	find . -name "__pycache__" -exec rm -rf {} \;
	rm -rf $(VENV) htmlcov

dev-env: | env
	$(PIP) install -r requirements/dev.txt

env:
	python -m venv $(VENV)
	$(PIP) install pip --upgrade
	$(PIP) install -r requirements/base.txt
