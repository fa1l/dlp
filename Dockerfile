FROM python:3.12
# Configure Poetry

RUN pip install poetry
RUN mkdir -p /app
COPY . /app

WORKDIR /app
# Install dependencies
ENV PATH="/app/.venv/bin:$PATH"

RUN poetry install