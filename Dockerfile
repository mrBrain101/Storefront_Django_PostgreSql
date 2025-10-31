FROM python:3.13.9-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    RUNNING_IN_CONTAINER=True \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    netcat-openbsd \
    dos2unix \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --upgrade pip && pip install pipenv

# Install application dependencies
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --dev --deploy

# Copy the application files
COPY . /app/

# Fix line endings and make scripts executable
RUN dos2unix /app/wait-for-it.sh /app/docker-entrypoint.sh && \
    chmod +x /app/wait-for-it.sh /app/docker-entrypoint.sh

# Create directories
RUN mkdir -p /app/media /app/static /app/conf /app/locustfiles

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]