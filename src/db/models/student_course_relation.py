from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import BaseModel


student_course_relation = Table(
    'student_course_relation',
    BaseModel.metadata,
    Column('student_id', Integer, ForeignKey('student_model.id')),
    Column('course_id', Integer, ForeignKey('course_model.id'))
)