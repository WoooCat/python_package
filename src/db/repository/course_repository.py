from typing import List, Optional

from .. import StudentCourseRelationModel
from ..models.course_model import CourseModel
from ..models.student_model import StudentModel
from .base_repository import BaseRepository


class CourseRepository(BaseRepository):
    def get_all_courses(self) -> List[CourseModel]:
        """Get all Courses"""
        return self.session.query(CourseModel).all()

    def get_course_by_id(self, course_id: int) -> Optional[CourseModel]:
        """Get Course by ID"""
        return self.session.query(CourseModel).filter_by(id=course_id).first()

    def create_course(self, name: str, description: str = None) -> Optional[CourseModel]:
        """Create Course"""
        course = CourseModel(name=name, description=description)
        self.session.add(course)

        self.session.commit()
        return course

    def update_course(self, course_id: int, name: str, description: str) -> Optional[CourseModel]:
        """Update Course"""
        course = self.get_course_by_id(course_id)
        if course:
            course.name = name
            course.description = description
            self.session.commit()
        return course

    def delete_course(self, course_id: int) -> Optional[CourseModel]:
        """Delete Course"""
        course = self.get_course_by_id(course_id)
        if course:
            self.session.delete(course)
            self.session.commit()
        return course

    def assign_student_to_course(self, course_id: int, student_id: int) -> Optional[StudentModel]:
        """Assign Student to Course"""
        course = self.get_course_by_id(course_id)
        student = self.session.query(StudentModel).get(student_id)
        if course and student:
            course.students.append(student)
            self.commit_changes()
            return student
        return None

    def remove_student_from_course(self, course_id: int, student_id: int) -> Optional[bool]:
        """Remove Student from Course"""
        course = self.get_course_by_id(course_id)
        student = self.session.query(StudentModel).get(student_id)
        if course and student:
            if student in course.students:
                course.students.remove(student)
                self.session.commit()
                return True
        return None

    def get_all_courses_for_student(self, student_id: int):
        """Get All Courses for Student"""
        return self.session.query(StudentCourseRelationModel).filter(StudentCourseRelationModel.student_id == student_id).all()