#!/usr/bin/env make -f

PROJECT_NAME  := rudy
PROJECT_ROOT  := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

REQUIREMENTS  := $(PROJECT_ROOT)/requirements.txt

VENV          := $(PROJECT_ROOT)/venv
VENV_SCRIPT   := $(VENV)/bin/$(PROJECT_NAME)
VENV_ACTIVATE := . $(VENV)/bin/activate

.PHONY: all clean run dist deps

all: dist

clean:
	rm -rf dist/
	rm -rf venv/
	rm -rf *.egg-info/

run: $(VENV_SCRIPT)
	$(VENV_ACTIVATE) && $(VENV_SCRIPT)

dist:
	python3 setup.py sdist

deps: $(VENV)
	$(VENV_ACTIVATE) && pip3 install -r $(REQUIREMENTS)

$(VENV_SCRIPT): $(VENV)
	$(MAKE) deps

$(VENV):
	python3 -mvenv $@
