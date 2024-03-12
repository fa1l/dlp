from celery_worker.settings import CelerySettings
from celery_worker.worker import create_celery_app
from dependencies.container import create_container

container = create_container()
settings = CelerySettings()
app = create_celery_app(container, settings)
