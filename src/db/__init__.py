from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.base import BaseModel
from .models.group_model import GroupModel
from .models.student_model import StudentModel
from .models.course_model import CourseModel
from .models.student_course_relation_model import StudentCourseRelationModel
from ..config import Config, config


def create_engine_with_config(env: Config):
    engine_config = config[env.value]
    app_engine = create_engine(engine_config.SQLALCHEMY_DATABASE_URI, echo=False)
    Session = sessionmaker(bind=app_engine)
    BaseModel.metadata.create_all(app_engine)
    return app_engine, Session


engine, Session = create_engine_with_config(Config.development)