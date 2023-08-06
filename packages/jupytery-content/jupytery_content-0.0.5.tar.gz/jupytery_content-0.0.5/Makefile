# Copyright (c) Datalayer, Inc. https://datalayer.io
# Distributed under the terms of the MIT License.

CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
CONDA_DEACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda deactivate
CONDA_REMOVE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda remove -y --all -n
# ENV_NAME=jupytery_auth
ENV_NAME=datalayer

.PHONY: clean build dist env key

.EXPORT_ALL_VARIABLES:

RAND="78026"
PROJECT_ID="jupytery-content-${RAND}"
SERVICE_ACCOUNT="example-${RAND}@${PROJECT_ID}.iam.gserviceaccount.com"
GOOGLE_APPLICATION_CREDENTIALS="${PWD}/gcp-key.json"
VERSION="0.0.1"

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
	rm gcp-key.json

env-rm:
	-conda remove -y --all -n ${ENV_NAME}

env:
	-conda env create -f environment.yml
	@echo 
	@echo -------------------------------------------
	@echo ✨  Jupytery Content environment is created.
	@echo -------------------------------------------
	@echo

install:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		pip install -e . )

start:
	echo open http://localhost:3000
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		yarn start )

test:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		GOOGLE_APPLICATION_CREDENTIALS=${GOOGLE_APPLICATION_CREDENTIALS} python -m unittest )

publish:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		rm -fr dist/* && \
		python setup.py sdist bdist_wheel && \
		twine upload dist/* )

repl:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		PYTHONPATH=./dist/jupytery-content-${VERSION}-py3-none-any.whl python )

key:
	gcloud iam service-accounts keys \
		create ${GOOGLE_APPLICATION_CREDENTIALS} \
		--project ${PROJECT_ID} \
		--iam-account ${SERVICE_ACCOUNT}
	chmod +r ${GOOGLE_APPLICATION_CREDENTIALS} 
	ls -alp ${GOOGLE_APPLICATION_CREDENTIALS}

jlab-gcp:
	($(CONDA_ACTIVATE) ${ENV_NAME}; \
		jupyter lab --config ./examples/gcp/jupyter_server_config.py )

docker-build:
	docker build \
		-t datalayer/jupyterlab-gcp:0.0.3 \
		-f ./Dockerfile \
		.

docker-push:
	docker push \
		datalayer/jupyterlab-gcp:0.0.3

docker-start: ## start the container.
	@exec echo open http://localhost:8888
	@exec docker run \
	  -it \
	  --rm \
	  --name gcp \
	  -p 8888:8888 \
	  datalayer/jupyterlab-gcp:0.0.3

docker-rm: ## remove the container.
	docker rm -f gcp

docker-connect: ## connect to the container.
	docker exec -it gcp bash

docker-logs: ## show container logs.
	docker logs gcp -f

docker-stop: ## stop the container.
	docker stop gcp
