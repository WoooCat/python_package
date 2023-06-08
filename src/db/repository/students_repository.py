from .base_repository import BaseRepository
from ..models.group_model import StudentModel


class StudentRepository(BaseRepository):
    def get_all_students(self):
        students = self.session.query(StudentModel).all()
        return students

    def get_student_by_id(self, student_id: int):
        student = self.session.query(StudentModel).get(student_id)
        return student

    def create_student(self, first_name: str, last_name: str, group_id=None):
        student = StudentModel(first_name=first_name, last_name=last_name, group_id=group_id)
        self.session.add(student)
        self.commit_changes()
        return student

    def update_student(self, student_id: int, first_name: str = None, last_name: str = None, group_id: int = None):
        student = self.get_student_by_id(student_id)
        if student:
            if first_name:
                student.first_name = first_name
            if last_name:
                student.last_name = last_name
            if group_id:
                student.group_id = group_id
            self.commit_changes()
        return student

    def delete_student(self, student_id: int):
        student = self.get_student_by_id(student_id)
        if student:
            self.session.delete(student)
            self.commit_changes()
        return student
