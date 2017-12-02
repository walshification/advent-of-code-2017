VENV     = $(CURDIR)/env
PIP      = $(VENV)/bin/pip
DEV_DEPS = install -r requirements/dev.txt

test: | $(VENV)/bin/coverage
	$(VENV)/bin/coverage run --rcfile=coverage.cfg -m unittest discover ./tests
	$(VENV)/bin/coverage report --rcfile=coverage.cfg
	$(VENV)/bin/coverage html --rcfile=coverage.cfg
	touch htmlcov

test-watch: | $(VENV)/bin/sniffer
	$(VENV)/bin/sniffer

shell: | $(VENV)/bin/ipython
	$(VENV)/bin/ipython

clean:
	find . -name "__pycache__" -exec rm -rf {} \;
	rm -rf $(VENV) htmlcov

$(VENV)/bin/ipython: | $(PIP)
	$(PIP) $(DEV_DEPS)

$(VENV)/bin/coverage: | $(PIP)
	$(PIP) $(DEV_DEPS)

$(VENV)/bin/sniffer: | $(PIP)
	$(PIP) $(DEV_DEPS)

$(PIP): | env
	$(PIP) install -r requirements/base.txt

env:
	python -m venv $(VENV)
	$(PIP) install pip --upgrade
