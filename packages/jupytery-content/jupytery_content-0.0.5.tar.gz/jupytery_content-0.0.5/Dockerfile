FROM jupyter/scipy-notebook:ubuntu-20.04

USER root

RUN apt-get update && apt-get install --yes --no-install-recommends \
    dnsutils \
    git \
    iputils-ping \
 && rm -rf /var/lib/apt/lists/*

USER $NB_USER

RUN mkdir /opt/conda/jupytery_content
COPY setup.py /opt/conda/jupytery_content
COPY jupytery_content /opt/conda/jupytery_content/jupytery_content
COPY README.md /opt/conda/jupytery_content
RUN pip install -e /opt/conda/jupytery_content

RUN python -m pip install --no-cache-dir \
    jupyterhub nbgitpuller

ARG PIP_OVERRIDES=
RUN if [[ -n "$PIP_OVERRIDES" ]]; then \
        pip install --no-cache-dir $PIP_OVERRIDES; \
    fi

RUN jupyter serverextension enable --py nbgitpuller --sys-prefix

ENV JUPYTER_ENABLE_LAB=true

COPY docker/conf.py /tmp/conf.py
RUN cat /tmp/conf.py >> /etc/jupyter/jupyter_server_config.py
RUN cat /tmp/conf.py >> /etc/jupyter/jupyter_notebook_config.py

# Uncomment the line below to make nbgitpuller default to start up in JupyterLab
# ENV NBGITPULLER_APP=lab

# conda/pip/apt install additional packages here, if desired.
