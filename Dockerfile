# syntax = docker/dockerfile:latest

FROM python:3.12-slim as python
ENV PYTHONUNBUFFERED=true
LABEL org.opencontainers.image.source="https://github.com/lanterno/archetype3"
LABEL authors="ahmed.elghareeb@proton.com"

FROM python as deps_builder

WORKDIR /deps
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_HOME=/deps/.poetry
ENV PATH="${POETRY_HOME}/bin:${PATH}"
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -

COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi -vvv

FROM python as runtime
COPY --from=deps_builder /deps/.venv /deps/.venv

WORKDIR /src
COPY . ./
ENV PATH="/deps/.venv/bin:$PATH"
EXPOSE 80

CMD ["gunicorn", "config.wsgi:application" , "--bind", "0.0.0.0:80", "--workers", "4"]
