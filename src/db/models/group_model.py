from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .student_model import StudentModel


class GroupModel(BaseModel):
    __tablename__ = 'group_model'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("StudentModel", back_populates="group")


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }