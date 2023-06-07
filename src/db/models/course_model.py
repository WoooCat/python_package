from sqlalchemy import Column, Integer, String

from .base import BaseModel



class CourseModel(BaseModel):
    __tablename__ = 'course_model'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }