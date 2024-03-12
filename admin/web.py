from flask import Flask
from flask_admin import Admin
from admin.views import LeakageView, RegexpView
from database import Session, DBLeakage, DBRegexpRule
from database.settings import DBSettings
from independency import Container

from regexp_getter.redis_getter import RedisRegexpGetter


def home_page() -> str:
    return """
    <p><a href="/admin/">Click me to get to Admin!</a></p>
    """


def create_admin(db_settings: DBSettings, container: Container):
    session = Session()
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_settings.url
    app.secret_key = "super secret key"
    app.add_url_rule("/", "home", view_func=home_page)

    admin = Admin(app, name="dlp_admin", template_mode="bootstrap4")
    regexp_view = RegexpView(DBRegexpRule, session)
    regexp_view.add_redis(container.resolve(RedisRegexpGetter))
    admin.add_view(regexp_view)
    admin.add_view(LeakageView(DBLeakage, session))
    return app
