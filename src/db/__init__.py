from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.base import Base
from .models.group_model import GroupModel
from .models.student_model import StudentModel
from .models.course_model import CourseModel
from .models.student_course_relation import student_course_relation
from src.config import DevelopmentConfig

engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)