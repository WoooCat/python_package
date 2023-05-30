from flask import request
from flask_restful import Resource
from src.db import Session
from src.db.repository.groups_repository import GroupRepository


class GroupResource(Resource):
    def __init__(self):
        self.session = Session()
        self.group_repo = GroupRepository(self.session)

    def get(self, group_id=None):
        try:
            if group_id is None:
                groups = self.group_repo.get_all_groups()
                return {'groups': [{'id': group.id, 'name': group.name} for group in groups]}
            else:
                group = self.group_repo.get_group_by_id(group_id)
                if group:
                    return {'id': group.id, 'name': group.name}
                else:
                    return {'error': 'Group not found'}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.group_repo.close_session()

    def post(self):
        try:
            data = request.get_json()
            name = data.get('name')
            group = self.group_repo.create_group(name)
            return {'message': 'Group created successfully', 'group_id': group.id}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.group_repo.close_session()

    def put(self, group_id):
        try:
            data = request.get_json()
            name = data.get('name')
            group = self.group_repo.update_group(group_id, name)
            if group:
                return {'message': 'Group updated successfully', 'group_id': group.id}
            else:
                return {'error': 'Group not found'}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.group_repo.close_session()

    def delete(self, group_id):
        try:
            group = self.group_repo.delete_group(group_id)
            if group:
                return {'message': 'Group deleted successfully', 'group_id': group.id}
            else:
                return {'error': 'Group not found'}
        except Exception as e:
            self.session.rollback()
            return {'error': str(e)}
        finally:
            self.group_repo.close_session()
