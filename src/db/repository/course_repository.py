from src.db import Session
from src.db.models.course_model import CourseModel


class CourseRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_courses(self):
        return self.session.query(CourseModel).all()

    def get_course_by_id(self, course_id):
        return self.session.query(CourseModel).filter_by(id=course_id).first()

    def create_course(self, name, description):
        course = CourseModel(name=name, description=description)
        self.session.add(course)
        self.session.commit()
        return course

    def update_course(self, course_id, name, description):
        course = self.get_course_by_id(course_id)
        if course:
            course.name = name
            course.description = description
            self.session.commit()
        return course

    def delete_course(self, course_id):
        course = self.get_course_by_id(course_id)
        if course:
            self.session.delete(course)
            self.session.commit()
        return course

    def close_session(self):
        self.session.close()
