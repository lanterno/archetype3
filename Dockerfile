# syntax = docker/dockerfile:latest

FROM python:3.12-slim as python
ENV PYTHONUNBUFFERED=true
LABEL org.opencontainers.image.source="https://github.com/lanterno/archetype3"
LABEL authors="ahmed.elghareeb@proton.com"

FROM python as deps_installer

ENV POETRY_HOME="/poetry"
ENV PATH="${POETRY_HOME}/bin:${PATH}"
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -

COPY pyproject.toml .
COPY poetry.lock .

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
RUN poetry config virtualenvs.create true
RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

FROM python as runtime

# Copy only necessary files from the deps_installer stage
WORKDIR /src
COPY . ./

COPY --from=deps_installer /.venv /deps/.venv

# Set the PATH to include the virtual environment
ENV PATH="/deps/.venv/bin:$PATH"

EXPOSE 80

CMD ["uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "80"]
