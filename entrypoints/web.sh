#!/bin/sh

set -e

. /app/.venv/bin/activate

exec uvicorn bin.web:fastapi_app --host 0.0.0.0