FROM python:3.10-slim AS build

# install poetry
RUN pip install poetry==1.4.2

# configure poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# configure Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY poetry.lock pyproject.toml ./
COPY flying_unicorns/ ./flying_unicorns
COPY README.md/ ./

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

ENV VIRTUAL_ENV=/app/.venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="/app/.venv/bin:$PATH"

RUN poetry version major
RUN poetry build

ARG UserCredential
ARG AccessToken

RUN twine upload -u ${UserCredential} -p ${AccessToken} --repository-url https://[somelink]/pypi/upload dist/*