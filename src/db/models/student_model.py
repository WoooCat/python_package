from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .student_course_relation import student_course_relation


class StudentModel(BaseModel):
    __tablename__ = 'student_model'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group_model.id'))
    first_name = Column(String)
    last_name = Column(String)
    group = relationship("GroupModel", back_populates="students")
    courses = relationship("CourseModel", secondary=student_course_relation, overlaps="students")

    def to_dict(self):
        serialized_data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'group': None,
            'courses': [course.to_dict() for course in self.courses]
        }
        if self.group:
            serialized_data['group'] = self.group.to_dict()
        return serialized_data
