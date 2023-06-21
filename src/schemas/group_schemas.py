from flask_restx import fields

from src.api_utils import api

create_group_schema = api.model("CreateGroup", {"name": fields.String(required=True, description="Group name")})

get_group_schema = api.model(
    "Group",
    {
        "id": fields.Integer(required=True, description="Group id"),
        "name": fields.String(required=True, description="Group name"),
    },
)
