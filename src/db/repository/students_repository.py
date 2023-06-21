from typing import List, Optional

from ..models.group_model import StudentModel
from .base_repository import BaseRepository


class StudentRepository(BaseRepository):
    def get_all_students(self) -> List[StudentModel]:
        """Get all Students"""
        return self.session.query(StudentModel).all()

    def get_student_by_id(self, student_id: int) -> Optional[StudentModel]:
        """Get Student by ID"""
        return self.session.query(StudentModel).get(student_id)

    def create_student(self, first_name: str, last_name: str, group_id=None) -> StudentModel:
        """Create Student"""
        student = StudentModel(first_name=first_name, last_name=last_name, group_id=group_id)
        self.session.add(student)
        self.commit_changes()
        return student

    def update_student(self, student_id: int, **kwargs) -> Optional[StudentModel]:
        """Update Student"""
        student = self.get_student_by_id(student_id)
        if student:
            for key, value in kwargs.items():
                if hasattr(student, key):
                    setattr(student, key, value)
            self.commit_changes()
        return student

    def delete_student(self, student_id: int) -> Optional[StudentModel]:
        """Delete Student"""
        student = self.get_student_by_id(student_id)
        if student:
            self.session.delete(student)
            self.commit_changes()
        return student
