from web.web import create_web_app
from dependencies.container import create_container

container = create_container()
fastapi_app = create_web_app(container)
