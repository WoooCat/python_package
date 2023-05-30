from .base_repository import BaseRepository
from ..models.group_model import GroupModel


class GroupRepository(BaseRepository):
    def get_all_groups(self):
        return self.session.query(GroupModel).all()

    def get_group_by_id(self, group_id):
        return self.session.query(GroupModel).get(group_id)

    def create_group(self, name):
        group = GroupModel(name=name)
        self.session.add(group)
        self.commit_changes()
        return group

    def update_group(self, group_id, name):
        group = self.get_group_by_id(group_id)
        if group:
            group.name = name
            self.commit_changes()
        return group

    def delete_group(self, group_id):
        group = self.get_group_by_id(group_id)
        if group:
            self.session.delete(group)
            self.commit_changes()
        return group
