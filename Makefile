# Variables
VENV_PATH=venv
PYTHON=$(VENV_PATH)/bin/python
PIP=$(VENV_PATH)/bin/pip
GUNICORN=$(VENV_PATH)/bin/gunicorn
APP_MODULE=main:app
HOST=0.0.0.0
PORT=8000
WORKERS=4

.PHONY: help install run start clean

# Help
help:
	@echo "Available commands:"
	@echo "  make install   - Set up virtual environment and install dependencies"
	@echo "  make run       - Run with Uvicorn (dev mode)"
	@echo "  make start     - Start with Gunicorn (prod mode)"
	@echo "  make clean     - Remove venv and __pycache__"

# Set up virtual environment and install packages
install:
	python3 -m venv $(VENV_PATH)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Development run with auto-reload
run:
	$(VENV_PATH)/bin/uvicorn $(APP_MODULE) --reload --host $(HOST) --port $(PORT)

# Production start with Gunicorn
start:
	$(GUNICORN) $(APP_MODULE) -k uvicorn.workers.UvicornWorker --bind $(HOST):$(PORT) --workers $(WORKERS)

# Clean environment
clean:
	rm -rf $(VENV_PATH)
	find . -type d -name "__pycache__" -exec rm -r {} +
