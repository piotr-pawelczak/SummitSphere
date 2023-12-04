FROM python:3.11-slim-bullseye AS build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install poetry

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        libpython3-dev \
        libpq-dev \
        gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy the Poetry configuration files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy the project code
COPY . /code/

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
