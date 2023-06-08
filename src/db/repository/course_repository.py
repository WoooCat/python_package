from typing import Optional
from .base_repository import BaseRepository
from ..models.course_model import CourseModel
from ..models.student_model import StudentModel


class CourseRepository(BaseRepository):

    def get_all_courses(self):
        courses = self.session.query(CourseModel).all()
        return courses

    def get_course_by_id(self, course_id: int):
        course = self.session.query(CourseModel).filter_by(id=course_id).first()
        return course

    def create_course(self, name: str, description: str) -> Optional[CourseModel]:
        course = CourseModel(name=name, description=description)
        self.session.add(course)
        self.session.commit()
        return course

    def update_course(self, course_id: int, name: str, description: str) -> Optional[CourseModel]:
        course = self.get_course_by_id(course_id)
        if course:
            course.name = name
            course.description = description
            self.session.commit()
        return course

    def delete_course(self, course_id: int) -> Optional[CourseModel]:
        course = self.get_course_by_id(course_id)

        if course:
            self.session.delete(course)
            self.session.commit()
        return course

    def assign_student_to_course(self, course_id: int, student_id: int) -> Optional[StudentModel]:
        course = self.get_course_by_id(course_id)
        student = self.session.query(StudentModel).get(student_id)

        if course and student:
            course.students.append(student)
            self.commit_changes()
            return student

    def remove_student_from_course(self, course_id: int, student_id: int) -> bool:
        course = self.get_course_by_id(course_id)
        student = self.session.query(StudentModel).get(student_id)

        if course and student:
            if student in course.students:
                course.students.remove(student)
                self.session.commit()
                return True
