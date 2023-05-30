from flask import Flask
from flask_restful import Api
from .api.v1.endpoints.groups_endpoints import GroupResource
from .api.v1.endpoints.students_endpoints import StudentResource
from .api.v1.endpoints.course_endpoints import CourseResource

app = Flask(__name__)
api = Api(app)


api.add_resource(GroupResource, '/groups', '/groups/<int:group_id>')
api.add_resource(StudentResource, '/students', '/students/<int:student_id>')
api.add_resource(CourseResource, '/courses', '/courses/<int:course_id>')

