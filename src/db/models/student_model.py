from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .student_course_relation import student_course_relation


class StudentModel(Base):
    __tablename__ = 'student_model'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group_model.id'))
    first_name = Column(String)
    last_name = Column(String)
    group = relationship("GroupModel", back_populates="students")
    courses = relationship("CourseModel", secondary=student_course_relation, overlaps="students")

