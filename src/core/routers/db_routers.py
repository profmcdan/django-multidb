from typing import Union


class BaseRouter:
    # this apps will read and write on the self.db_name
    route_app_labels = {}
    db_name = ''

    def db_for_read(self, model, **hints) -> Union[str, None]:
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints) -> Union[str, None]:
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints) -> Union[bool, None]:
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints) -> Union[bool, None]:
        if db == self.db_name:
            return app_label in self.route_app_labels
        elif app_label in self.route_app_labels:
            return False
        return None


class UserRouter(BaseRouter):
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin', 'user'}
    db_name = 'user_db'


class StudentRouter(BaseRouter):
    route_app_labels = {'student'}
    db_name = 'student_db'


class TeacherRouter(BaseRouter):
    route_app_labels = {'teacher'}
    db_name = 'teacher_db'
