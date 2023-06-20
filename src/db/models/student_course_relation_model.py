from sqlalchemy import Column, Integer, ForeignKey
from .base import BaseModel


class StudentCourseRelationModel(BaseModel):
    __tablename__ = "student_course_relation"

    student_id = Column(Integer, ForeignKey("student_model.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("course_model.id"), primary_key=True)
