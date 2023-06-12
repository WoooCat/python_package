from flask_restx import Api, fields

api = Api(default="UNIVERSITY API ", default_label="Full CRUD API for University")

doc_group_model = api.model("Group", {"name": fields.String(required=True, description="Group name")})

doc_student_model = api.model(
    "Student",
    {
        "id": fields.Integer(description="Student ID"),
        "first_name": fields.String(required=True, description="First name"),
        "last_name": fields.String(required=True, description="Last name"),
    },
)

doc_course_model = api.model(
    "Course",
    {
        "name": fields.String(required=True, description="Course name"),
        "description": fields.String(description="Course Description"),
    },
)
