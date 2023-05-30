from flask import request
from flask_restful import Resource
from src.db import Session
from src.db.repository.students_repository import StudentRepository


class StudentResource(Resource):
    def __init__(self):
        self.session = Session()
        self.student_repo = StudentRepository(self.session)

    def get(self, student_id=None):
        try:
            if student_id is None:
                students = self.student_repo.get_all_students()
                return {'students': [{'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name} for student in students]}
            else:
                student = self.student_repo.get_student_by_id(student_id)
                if student:
                    return {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name}
                else:
                    return {'error': 'Student not found'}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.student_repo.close_session()

    def post(self):
        try:
            data = request.get_json()
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            student = self.student_repo.create_student(first_name, last_name)
            return {'message': 'Student created successfully', 'student_id': student.id}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.student_repo.close_session()

    def put(self, student_id):
        try:
            data = request.get_json()
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            student = self.student_repo.update_student(student_id, first_name, last_name)
            if student:
                return {'message': 'Student updated successfully', 'student_id': student.id}
            else:
                return {'error': 'Student not found'}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.student_repo.close_session()

    def delete(self, student_id):
        try:
            student = self.student_repo.delete_student(student_id)
            if student:
                return {'message': 'Student deleted successfully', 'student_id': student.id}
            else:
                return {'error': 'Student not found'}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.student_repo.close_session()