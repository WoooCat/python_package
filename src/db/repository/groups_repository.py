from typing import List, Optional

from ..models.group_model import GroupModel
from ..models.student_model import StudentModel
from .base_repository import BaseRepository


class GroupRepository(BaseRepository):
    def get_all_groups(self) -> List[GroupModel]:
        """Get all Groups"""
        return self.session.query(GroupModel).all()

    def get_group_by_id(self, group_id: int) -> Optional[GroupModel]:
        """Get Group by ID"""
        return self.session.query(GroupModel).get(group_id)

    def create_group(self, name: str) -> GroupModel:
        """Create Group"""
        group = GroupModel(name=name)
        self.session.add(group)
        self.commit_changes()
        return group

    def update_group(self, group_id: int, name: str) -> Optional[GroupModel]:
        """Update Group"""
        group = self.get_group_by_id(group_id)
        if group:
            group.name = name
        return group

    def delete_group(self, group_id: int) -> Optional[GroupModel]:
        """Delete Group"""
        group = self.get_group_by_id(group_id)
        if group:
            self.session.delete(group)
            self.commit_changes()
        return group

    def assign_student_to_group(self, group_id: int, student_id: int) -> Optional[StudentModel]:
        """Assign Student to Group"""
        group = self.get_group_by_id(group_id)
        student = self.session.query(StudentModel).get(student_id)
        if group and student:
            student.group_id = group_id
            self.commit_changes()
            return student
        return None

    def remove_student_from_group(self, group_id: int, student_id: int) -> Optional[StudentModel]:
        """Remove Student from Group"""
        group = self.get_group_by_id(group_id)
        student = self.session.query(StudentModel).get(student_id)
        if group and student:
            if student.group_id:
                student.group_id = None
                self.commit_changes()
                return student
        return None
