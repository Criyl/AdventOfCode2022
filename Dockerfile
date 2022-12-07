ARG PYTHON_VERSION="3.10"
FROM python:${PYTHON_VERSION}-slim-buster

RUN pip install poetry

WORKDIR /opt/app

COPY pyproject.toml poetry.lock /opt/app/
RUN poetry install --no-interaction

COPY . .
