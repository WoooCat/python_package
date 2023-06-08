from flask import request
# from flask_restful import Resource
from flask_restx import Resource
from src.db import Session
from src.db.repository.students_repository import StudentRepository


class StudentResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = Session()
        self.student_repo = StudentRepository(self.session)

    def get(self, student_id=None):
        if not student_id:
            students = self.student_repo.get_all_students()
            return {'students': [student.to_dict() for student in students]}, 200
        else:
            student = self.student_repo.get_student_by_id(student_id)
            if student:
                return student.to_dict(), 200
            else:
                return {'error': 'Student not found'}, 404

    def post(self):
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        student = self.student_repo.create_student(first_name, last_name)
        return student.to_dict(), 201

    def put(self, student_id):
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        student = self.student_repo.update_student(student_id, first_name, last_name)
        if student:
            return student.to_dict(), 200
        else:
            return {'error': 'Student not found'}, 404

    def delete(self, student_id):
        student = self.student_repo.delete_student(student_id)
        if student:
            return {'message': 'Student removed successfully'}, 200
        else:
            return {'error': 'Student not found'}, 404
