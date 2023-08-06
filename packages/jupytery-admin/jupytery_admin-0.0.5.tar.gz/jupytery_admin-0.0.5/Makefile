# Copyright (c) Datalayer, Inc. https://datalayer.io
# Distributed under the terms of the MIT License.

CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
CONDA_DEACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda deactivate
CONDA_REMOVE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda remove -y --all -n
# ENV_NAME=jupytery-admin
ENV_NAME=datalayer

.PHONY: clean build dist env cp

.EXPORT_ALL_VARIABLES:

VERSION = 0.0.1

default: all ## Default target is all.

help: ## display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

all: clean install build dist ## Clean, install and build.

build:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		yarn build )

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
	@echo -----------------------------------------
	@echo ✨  Jupyter Admin environment is created.
	@echo -----------------------------------------
	@echo

install:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		pip install -e . && \
		yarn install )

publish:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		rm -fr dist/* && \
		python setup.py sdist bdist_wheel && \
		twine upload dist/* )

repl:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		PYTHONPATH=./dist/jupytery_admin-${VERSION}-py3-none-any.whl python )

start:
	echo open http://localhost:2003
	echo open http://localhost:8686/hub/jupytery-admin
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		yarn start )

jupyterhub:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		yarn start:jupyterhub)

jupyterhub-rbac:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		rm -fr jupyterhub || true && \
		git clone https://github.com/jupyterhub/jupyterhub && \
			pip install -e . )

jupyterhub-token:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		jupyterhub token ${USER} )

jupyterhub-js:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		rm -fr dist/* || true && \
		yarn build:prod && \
		rm share/jupyterhub/jupytery-admin/static/js/*.js || true && \
		cp dist/*.js share/jupyterhub/jupytery-admin/static/js/ )

jupyterhub-sqlite:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		sqlite3 ./jupyterhub.sqlite )
