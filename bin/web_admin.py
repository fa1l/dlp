from admin import create_admin
from database.settings import DBSettings
from dependencies.container import create_container

settings = DBSettings()
container = create_container()
app = create_admin(settings, container)
app.run(host="0.0.0.0", port=8001)
