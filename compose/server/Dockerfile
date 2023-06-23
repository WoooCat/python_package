FROM python:3.11.3-slim-buster as base

ENV APP_HOME=/home/app \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.4.0 \
    POETRY_HOME=/home/app/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Create user
RUN groupadd -r api && \
useradd -r -g api -d $APP_HOME -s /sbin/nologin -c "Docker image User" tester

WORKDIR $APP_HOME

# Install dependencies
RUN pip install --upgrade pip
RUN curl - sSL https://install.python-poetry.org | python -
RUN pip install poetry

COPY pyproject.toml /
RUN poetry install

# Run app
CMD ["python3", "/app/main.py"]
