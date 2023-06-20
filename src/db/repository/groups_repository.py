from .base_repository import BaseRepository
from ..models.group_model import GroupModel
from ..models.student_model import StudentModel
from typing import List, Optional


class GroupRepository(BaseRepository):
    def get_all_groups(self) -> List[GroupModel]:
        groups = self.session.query(GroupModel).all()
        return groups

    def get_group_by_id(self, group_id: int) -> Optional[GroupModel]:
        return self.session.query(GroupModel).get(group_id)

    def create_group(self, name: str) -> GroupModel:
        group = GroupModel(name=name)
        self.session.add(group)
        self.commit_changes()
        return group

    def update_group(self, group_id: int, name: str) -> Optional[GroupModel]:
        group = self.get_group_by_id(group_id)
        if group:
            group.name = name
        return group

    def delete_group(self, group_id: int) -> Optional[GroupModel]:
        group = self.get_group_by_id(group_id)
        if group:
            self.session.delete(group)
            self.commit_changes()
        return group

    def assign_student_to_group(self, group_id: int, student_id: int) -> Optional[StudentModel]:
        group = self.get_group_by_id(group_id)
        student = self.session.query(StudentModel).get(student_id)
        if group and student:
            student.group_id = group_id
            self.commit_changes()
            return student

    def remove_student_from_group(self, group_id: int, student_id: int) -> bool:
        group = self.get_group_by_id(group_id)
        student = self.session.query(StudentModel).get(student_id)
        if group and student:
            if student.group_id:
                student.group_id = None
                self.commit_changes()
                return student
