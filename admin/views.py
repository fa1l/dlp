from flask_admin.contrib import sqla


class RegexpView(sqla.ModelView):
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
