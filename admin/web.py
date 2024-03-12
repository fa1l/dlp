from flask import Flask
from flask_admin import Admin
from admin.views import LeakageView, RegexpView
from database import Session, DBLeakage, DBRegexpRule
from database.settings import DBSettings


def home_page() -> str:
    return """
    <p><a href="/admin/">Click me to get to Admin!</a></p>
    """


def create_admin(db_settings: DBSettings):
    session = Session()
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_settings.url
    app.secret_key = "super secret key"
    app.add_url_rule("/", "home", view_func=home_page)

    admin = Admin(app, name="dlp_admin", template_mode="bootstrap4")
    admin.add_view(RegexpView(DBRegexpRule, session))
    admin.add_view(LeakageView(DBLeakage, session))
    return app
