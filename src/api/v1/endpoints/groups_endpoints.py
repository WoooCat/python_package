from flask import request
from flask_restx import Resource

from src.api_utils import api, doc_group_model
from src.db import Session
from src.db.repository.groups_repository import GroupRepository


class GroupResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = Session()
        self.group_repo = GroupRepository(self.session)

    def get(self, group_id=None):
        """Get a group by ID or retrieve all groups"""
        if not group_id:
            groups = self.group_repo.get_all_groups()
            return {"groups": [group.to_dict() for group in groups]}, 200
        else:
            group = self.group_repo.get_group_by_id(group_id)
            if group:
                return group.to_dict(), 200
            else:
                return {"error": "Group not found"}, 404

    @api.expect(doc_group_model)
    def post(self):
        """Create a new group"""
        data = request.get_json()
        name = data.get("name")
        group = self.group_repo.create_group(name)
        return group.to_dict(), 201

    @api.expect(doc_group_model)
    def put(self, group_id):
        """Update a group by ID"""
        data = request.get_json()
        name = data.get("name")
        group = self.group_repo.update_group(group_id, name)
        if group:
            return group.to_dict(), 200
        else:
            return {"error": "Group not found"}, 404

    def delete(self, group_id):
        """Delete a group by ID"""
        group = self.group_repo.delete_group(group_id)
        if group:
            return {"message": "Group removed successfully"}, 200
        else:
            return {"error": "Group not found"}, 404


class GroupStudentResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = Session()
        self.group_repository = GroupRepository(self.session)

    def put(self, group_id, student_id):
        """Assign Student to Group"""
        group_student = self.group_repository.assign_student_to_group(group_id, student_id)
        if group_student:
            return {"message": f"Student with id: {student_id} successfully added to the group"}, 200
        else:
            return {"message": f"Group with id: '{group_id}' or Student with id: '{student_id}' not found"}, 404

    def delete(self, group_id, student_id):
        """Remove Student from Group"""
        group = self.group_repository.remove_student_from_group(group_id, student_id)
        if group:
            return {"message": f"Student with id: {student_id} successfully removed from Group"}, 200
        else:
            return {"message": f"Group with id: '{group_id}' or Student with id: '{student_id}' not found"}, 404
