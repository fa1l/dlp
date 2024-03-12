import re
from flask_admin.contrib import sqla
from sqlalchemy import select

from database.regexp_rule import DBRegexpRule
from regexp_getter.redis_getter import RedisRegexpGetter


class RegexpView(sqla.ModelView):
    redis_db = None

    column_display_pk = True
    column_list = [
        "id",
        "name",
        "regexp",
        "created_at",
    ]
    column_default_sort = ("id", True)
    create_modal = True
    edit_modal = True

    def add_redis(self, redis: RedisRegexpGetter):
        self.redis_db = redis

    def after_model_change(self, form, model, is_created):
        statement = select(DBRegexpRule)
        regexps = self.session.scalars(statement).all()
        results = []

        for data in regexps:
            pattern = re.compile(data.regexp)
            results.append(pattern)
        self.redis_db.remove_regexps()
        self.redis_db.add_regexps(results)


class LeakageView(sqla.ModelView):
    column_display_pk = True
    column_list = [
        "id",
        "message",
        "content",
        "pattern",
        "created_at",
    ]
    column_default_sort = ("id", True)
    can_create = False
    can_edit = False
    can_delete = False
