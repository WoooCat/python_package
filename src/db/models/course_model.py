from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import BaseModel
from .student_model import student_course_relation


class CourseModel(BaseModel):
    __tablename__ = "course_model"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    students = relationship("StudentModel", secondary=student_course_relation, back_populates="courses")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}
