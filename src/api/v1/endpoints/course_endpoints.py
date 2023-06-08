from flask import request
# from flask_restful import Resource
from flask_restx import Resource
from src.db import Session
from src.db.repository.course_repository import CourseRepository
from src.db.repository.students_repository import StudentRepository


class CourseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = Session()
        self.course_repo = CourseRepository(self.session)

    def get(self, course_id=None):
        if not course_id:
            courses = self.course_repo.get_all_courses()
            return {'courses': [course.to_dict() for course in courses]}, 200
        else:
            course = self.course_repo.get_course_by_id(course_id)
            if course:
                return course.to_dict(), 200
            else:
                return {'error': 'Course not found'}, 404

    def post(self):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        group = self.course_repo.create_course(name=name, description=description)
        return group.to_dict(), 201

    def put(self, course_id):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        course = self.course_repo.update_course(course_id=course_id, name=name, description=description)
        if course:
            return course.to_dict(), 200
        else:
            return {'error': 'Course not found'}, 404

    def delete(self, course_id):
        course = self.course_repo.delete_course(course_id)
        if course:
            return {'message': 'Course deleted successfully', 'course_id': course.id}, 200
        else:
            return {'error': 'Course not found'}, 404


class CourseStudentResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = Session()
        self.course_repository = CourseRepository(self.session)
        self.student_repository = StudentRepository(self.session)

    def put(self, course_id, student_id):
        course_student = self.course_repository.assign_student_to_course(course_id, student_id)
        if course_student:
            return {"message": f"Student with id: {student_id} successfully added to the Course"}, 200
        else:
            return {"message": f"Course with id: '{course_id}' or Student with id: '{student_id}' not found"}, 404

    def patch(self, course_id, student_id):
        course_student = self.course_repository.remove_student_from_course(course_id, student_id)
        if course_student:
            return {"message": f"Student with id: {student_id} successfully removed from Course"}, 200
        else:
            return {"message": f"Course with id: '{course_id}' or Student with id: '{student_id}' not found"}, 404
