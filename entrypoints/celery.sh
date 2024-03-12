#!/bin/sh

set -e

. /app/.venv/bin/activate

exec celery -A bin.celery_app.app worker --loglevel=INFO