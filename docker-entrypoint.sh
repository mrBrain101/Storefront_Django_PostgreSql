#!/bin/bash
set -e

echo "=== Starting Django Application ==="

# Wait a moment for database to be fully ready
sleep 2

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files (for production)
if [ "$DJANGO_SETTINGS_MODULE" = "storefront.settings.prod" ]; then
    echo "Collecting static files for production..."
    python manage.py collectstatic --noinput --clear || true
fi

# Create superuser only if DEBUG=True
if [ "$DEBUG" = "True" ] || [ "$DEBUG" = "true" ]; then
    echo "DEBUG mode detected. Creating superuser if it doesn't exist..."
    python manage.py createsuperuser --noinput || true
fi

# Run population script if POPULATE_DB is true
if [ "$POPULATE_DB" = "True" ] || [ "$POPULATE_DB" = "true" ]; then
    echo "POPULATE_DB is true. Populating database and incrementing IDs..."
    python manage.py seed_db
fi

echo "Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000