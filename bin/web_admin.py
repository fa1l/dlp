from admin import create_admin
from database.settings import DBSettings

settings = DBSettings()
app = create_admin(settings)
app.run()
