from celery import Celery
from independency import Container

from celery_worker.settings import CelerySettings
from celery_worker.task import LeakFinderTask
from leak_finder.regexp import RegexpLeakFinder


def create_celery_app(container: Container, settings: CelerySettings) -> Celery:
    celery_app = Celery(__name__)
    celery_app.conf.broker_url = settings.broker_url
    celery_app.conf.result_backend = settings.result_backend
    celery_app.register_task(LeakFinderTask(container.resolve(RegexpLeakFinder)))
    return celery_app
