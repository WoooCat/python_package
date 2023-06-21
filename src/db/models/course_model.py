from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import BaseModel
from .student_course_relation_model import StudentCourseRelationModel


class CourseModel(BaseModel):
    __tablename__ = "course_model"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    students = relationship("StudentModel", secondary=StudentCourseRelationModel.__table__, back_populates="courses")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}
