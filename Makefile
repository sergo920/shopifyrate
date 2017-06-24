SHELL = /bin/bash

.PHONY: clean build

default:
	echo "This is a Makefile of 'Shopify Rate' project"

clean:
	rm -rf $(BUILD_OUTPUT_PATH)/*

.PHONY: venv
venv:
	./bin/setup-virtualenv.sh ${PWD} ${VENV_DIR}

.PHONY: touch
app-touch:
	touch ./shopifyrate/wsgi.py
