from flask import request
from flask_restful import Resource
from src.db import Session
from src.db.repository.course_repository import CourseRepository


class CourseResource(Resource):
    def __init__(self):
        self.session = Session()
        self.course_repo = CourseRepository(self.session)

    def get(self, course_id=None):
        try:
            if course_id is None:
                courses = self.course_repo.get_all_courses()
                return {'courses': [{'id': course.id, 'name': course.name, 'description': course.description} for course in courses]}
            else:
                course = self.course_repo.get_course_by_id(course_id)
                if course:
                    return {'id': course.id, 'name': course.name, 'description': course.description}
                else:
                    return {'error': 'Course not found'}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.course_repo.close_session()

    def post(self):
        try:
            data = request.get_json()
            name = data.get('name')
            description = data.get('description')
            course = self.course_repo.create_course(name, description)
            return {'message': 'Course created successfully', 'course_id': course.id}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.course_repo.close_session()

    def put(self, course_id):
        try:
            data = request.get_json()
            name = data.get('name')
            description = data.get('description')
            course = self.course_repo.update_course(course_id, name, description)
            if course:
                return {'message': 'Course updated successfully', 'course_id': course.id}
            else:
                return {'error': 'Course not found'}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.course_repo.close_session()

    def delete(self, course_id):
        try:
            course = self.course_repo.delete_course(course_id)
            if course:
                return {'message': 'Course deleted successfully', 'course_id': course.id}
            else:
                return {'error': 'Course not found'}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.course_repo.close_session()
