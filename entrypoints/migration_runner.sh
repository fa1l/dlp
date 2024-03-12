#!/bin/sh

set -e

. /app/.venv/bin/activate

exec alembic upgrade head