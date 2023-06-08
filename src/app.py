from flask import Flask, g
from flask_restful import Api
from .api.v1.endpoints.groups_endpoints import GroupResource, GroupStudentResource
from .api.v1.endpoints.students_endpoints import StudentResource
from .api.v1.endpoints.course_endpoints import CourseResource, CourseStudentResource

app = Flask(__name__)
api = Api(app)


api.add_resource(GroupResource, '/groups', '/groups/<int:group_id>')
api.add_resource(StudentResource, '/students', '/students/<int:student_id>')
api.add_resource(GroupStudentResource, '/groups/<int:group_id>/students/<int:student_id>')
api.add_resource(CourseResource, '/courses', '/courses/<int:course_id>')
api.add_resource(CourseStudentResource, '/course/<int:course_id>/student/<int:student_id>')


# @app.errorhandler(Exception)
# def handle_error(error):
#     app.logger.error(f"An error occurred: {str(error)}")
#     return {'error': 'Internal Server Error'}, 500
