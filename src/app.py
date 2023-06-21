from flask import Flask

from .api.v1.endpoints.course_endpoints import CourseResource, CourseStudentResource
from .api.v1.endpoints.groups_endpoints import GroupResource, GroupStudentResource
from .api.v1.endpoints.students_endpoints import StudentResource
from .api_utils import api


def create_app():
    # app
    app = Flask(__name__)

    # api
    api.init_app(app)
    api.add_resource(GroupResource, "/groups", "/groups/<int:group_id>")
    api.add_resource(StudentResource, "/students", "/students/<int:student_id>")
    api.add_resource(GroupStudentResource, "/groups/<int:group_id>/students/<int:student_id>")
    api.add_resource(CourseResource, "/course", "/course/<int:course_id>")
    api.add_resource(CourseStudentResource, "/course/<int:course_id>/student/<int:student_id>")

    return app
