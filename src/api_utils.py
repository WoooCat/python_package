from flask_restx import Api, fields

api = Api(default="UNIVERSITY API ", prefix="/api/v1", default_label="FULL CRUD API <FLASK + POSTGRESQL> ")


doc_course_model = api.model(
    "Course",
    {
        "name": fields.String(required=True, description="Course name"),
        "description": fields.String(description="Course Description"),
    },
)
