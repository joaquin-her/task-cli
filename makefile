
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest
run: $(VENV)/bin/activate
	$(PYTHON) app.py

setup: requirements.txt
	$(PIP) install -r requirements.txt

test: 
	$(PYTEST) tests -v

clean:
	rm -rf __pycache__
	rm -rf $(VENV)

