from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .student_course_relation_model import StudentCourseRelationModel


class StudentModel(BaseModel):
    __tablename__ = "student_model"
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("group_model.id"))
    first_name = Column(String)
    last_name = Column(String)
    group = relationship("GroupModel", back_populates="students")
    courses = relationship("CourseModel", secondary=StudentCourseRelationModel.__table__, overlaps="students")

    def to_dict(self):
        serialized_data = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "group": None,
            "courses": [course.to_dict() for course in self.courses],
        }
        if self.group:
            serialized_data["group"] = self.group.to_dict()
        return serialized_data
