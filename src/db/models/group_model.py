from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .student_model import StudentModel


class GroupModel(Base):
    __tablename__ = 'group_model'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("StudentModel", back_populates="group")
