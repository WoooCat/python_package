from flask_restx import fields

from src.api_utils import api

create_course_schema = api.model(
    "CreateCourse",
    {
        "name": fields.String(required=True, description="Course name"),
        "description": fields.String(description="Course Description"),
    },
)

get_course_schema = api.model(
    "Course",
    {
        "id": fields.Integer(description="Course id"),
        "name": fields.String(required=True, description="Course name"),
        "description": fields.String(description="Course Description"),
    },
)
