
VENV = task-cli-venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip


venv: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

docker_build:
        docker build -t task-cli-linux .

docker_up:
        docker_build
        docker run -it \
                -v $(PWD)/src:/task-cli/src \
                -v $(PWD)/tests:/task-cli/tests \
                -v $(PWD)/task-cli.py:/task-cli/task-cli.py \
                -v $(PWD)/makefile:/task-cli/makefile \
                task-cli-linux

clean:
	rm -rf __pycache__
	rm -rf $(VENV)

