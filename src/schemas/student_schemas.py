from flask_restx import fields

from src.api_utils import api

doc_student_model = api.model(
    "Student",
    {
        "id": fields.Integer(description="Student ID"),
        "first_name": fields.String(required=True, description="First name"),
        "last_name": fields.String(required=True, description="Last name"),
    },
)

create_update_student_schema = api.model(
    "PostStudentModel",
    {
        "first_name": fields.String(required=True, description="First name"),
        "last_name": fields.String(required=True, description="Last name"),
    },
)

get_student_schema = api.model(
    "StudentModel",
    {
        "id": fields.Integer(description="Student ID"),
        "first_name": fields.String(required=True, description="First name"),
        "last_name": fields.String(required=True, description="Last name"),
        "group": fields.Nested(
            api.model(
                "GroupModel",
                {
                    "id": fields.Integer(description="Group ID"),
                    "name": fields.String(required=True, description="Group name"),
                },
            )
        ),
        "courses": fields.List(
            fields.Nested(
                api.model(
                    "CourseModel",
                    {
                        "id": fields.Integer(description="Course ID"),
                        "name": fields.String(required=True, description="Course name"),
                        "description": fields.String(description="Course description"),
                    },
                )
            )
        ),
    },
)
