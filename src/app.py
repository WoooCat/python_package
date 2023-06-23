from flask import Flask

from .api.v1.endpoints.course_endpoints import CourseResource, CourseStudentResource, CoursesResource
from .api.v1.endpoints.groups_endpoints import GroupResource, GroupStudentResource, GroupsResource
from .api.v1.endpoints.students_endpoints import StudentResource, StudentsResource
from .api_utils import api


def create_app():
    # app
    app = Flask(__name__)

    # api
    api.init_app(app)
    api.add_resource(GroupsResource, "/groups/")
    api.add_resource(GroupResource, "/groups/", "/groups/<int:group_id>")
    api.add_resource(StudentsResource, "/students/")
    api.add_resource(StudentResource, "/students/", "/students/<int:student_id>")
    api.add_resource(GroupStudentResource, "/groups/<int:group_id>/students/<int:student_id>")
    api.add_resource(CoursesResource, "/courses/")
    api.add_resource(CourseResource, "/courses/", "/courses/<int:course_id>")
    api.add_resource(CourseStudentResource, "/courses/<int:course_id>/students/<int:student_id>")

    return app
