from sqlalchemy import Column, Integer, String
from .base import Base


class CourseModel(Base):
    __tablename__ = 'course_model'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
