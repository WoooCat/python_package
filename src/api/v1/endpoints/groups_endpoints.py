from typing import Any, Dict, Tuple, List, Union

from flask import request
from flask_restx import Resource

from src.api_utils import api
from src.db import Session
from src.db.repository.groups_repository import GroupRepository
from src.schemas.group_schemas import create_group_schema, get_group_schema


class GroupsResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.doc(model=get_group_schema)
    def get(self) -> Tuple[Dict[str, List[Dict[str, Any]]], int]:
        """Get all groups"""
        session = Session()
        group_repo = GroupRepository(session)
        groups = group_repo.get_all_groups()
        return {"groups": [group.to_dict() for group in groups]}, 200


class GroupResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.doc(model=get_group_schema)
    def get(self, group_id: int = None) -> Tuple[Union[Dict[str, str], Any], int]:
        """Get a group by ID"""
        session = Session()
        group_repo = GroupRepository(session)
        group = group_repo.get_group_by_id(group_id)
        if group:
            return group.to_dict(), 200
        else:
            return {"error": "Group not found"}, 404


    @api.expect(create_group_schema)
    @api.response(201, 'Group created successfully', model=get_group_schema)
    def post(self) -> Tuple[Dict[str, Any], int]:
        """Create a new group"""
        session = Session()
        group_repo = GroupRepository(session)
        data = request.get_json()
        name = data.get("name")
        group = group_repo.create_group(name)
        return group.to_dict(), 201

    @api.doc(model=get_group_schema)
    @api.expect(create_group_schema)
    def patch(self, group_id: int) -> Tuple[Dict[str, Any], int]:
        """Update a group by ID"""
        session = Session()
        group_repo = GroupRepository(session)
        data = request.get_json()
        name = data.get("name")
        group = group_repo.update_group(group_id, name)
        if group:
            return group.to_dict(), 200
        else:
            return {"error": "Group not found"}, 404

    def delete(self, group_id: int) -> Tuple[Dict[str, Any], int]:
        """Delete a group by ID"""
        session = Session()
        group_repo = GroupRepository(session)
        group = group_repo.delete_group(group_id)
        if group:
            return {"message": "Group removed successfully"}, 200
        else:
            return {"error": "Group not found"}, 404


class GroupStudentResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self, group_id: int, student_id: int) -> Tuple[Dict[str, str], int]:
        """Assign Student to Group"""
        session = Session()
        group_repository = GroupRepository(session)
        group_student = group_repository.assign_student_to_group(group_id, student_id)
        if group_student:
            return {"message": f"Student with id: '{student_id}' successfully added to the group"}, 200
        else:
            return {"message": f"Group with id: '{group_id}' or Student with id: '{student_id}' not found"}, 404

    def delete(self, group_id: int, student_id: int) -> Tuple[Dict[str, str], int]:
        """Remove Student from Group"""
        session = Session()
        group_repository = GroupRepository(session)
        group = group_repository.remove_student_from_group(group_id, student_id)
        if group:
            return {"message": f"Student with id: '{student_id}' successfully removed from Group"}, 200
        else:
            return {"message": f"Group with id: '{group_id}' or Student with id: '{student_id}' not found"}, 404
