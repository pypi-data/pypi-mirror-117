# Copyright (c) Datalayer, Inc. https://datalayer.io
# Distributed under the terms of the MIT License.

CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
CONDA_DEACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda deactivate
CONDA_REMOVE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda remove -y --all -n
# ENV_NAME=jupytery_auth
ENV_NAME=datalayer

.PHONY: clean build dist env cp

.EXPORT_ALL_VARIABLES:

VERSION = 0.0.1

default: all ## Default target is all.

help: ## display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

all: clean install build dist ## Clean, install and build.

clean:
	rm -fr build
	rm -fr dist
	rm -fr *.egg-info
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm jupyterhub.sqlite

env-rm:
	-conda remove -y --all -n ${ENV_NAME}

env:
	-conda env create -f environment.yml
	@echo 
	@echo ----------------------------------------
	@echo ✨  Jupytery Auth environment is created.
	@echo ----------------------------------------
	@echo

install:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		pip install -e . && \
		yarn install )

yarn-build:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		yarn build )

build:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
	  jupyter labextension develop --overwrite && \
		jupyter labextension list && \
		pip list | grep ${ENV_NAME} )

jupyterlab-start-watch:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		echo open http://localhost:8686 && \
		jupyter lab \
			--port 8686 \
			--watch \
			--ServerApp.base_url='/example' \
			--ServerApp.default_url='/example/lab' \
			--ServerApp.jpserver_extensions="{'jupytery_auth': True, 'jupyterlab': True}" \
			--ServerApp.login_handler_class=jupytery_auth.authentication.github.LoginHandler \
			--notebook-dir=./examples/notebooks )

start:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		yarn start )

publish:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		rm -fr dist/* && \
		python setup.py sdist bdist_wheel && \
		twine upload dist/* )
