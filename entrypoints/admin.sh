#!/bin/sh

set -e

. /app/.venv/bin/activate
export PYTHONPATH=.

exec python3 bin/web_admin.py