from typing import Any, Dict, List, Tuple, Union

from flask import request
from flask_restx import Resource

from src.api_utils import api
from src.db import Session
from src.db.repository.students_repository import StudentRepository
from src.schemas.student_schemas import create_update_student_schema, get_student_schema


class StudentsResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.doc(model=get_student_schema)
    def get(self) -> Tuple[Dict[str, List], int]:
        """Get all Students"""
        session = Session()
        students_repo = StudentRepository(session)
        students = students_repo.get_all_students()
        return {"students": [student.to_dict() for student in students]}, 200


class StudentResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.doc(model=get_student_schema)
    def get(self, student_id: int = None) -> Tuple[Union[Dict[str, Any], Tuple[List[Dict[str, Any]], int]], int]:
        """Get Student by ID or all Students"""
        session = Session()
        student_repo = StudentRepository(session)
        student = student_repo.get_student_by_id(student_id)
        if student:
            return student.to_dict(), 200
        else:
            return {"error": "Student not found"}, 404

    @api.doc(model=get_student_schema)
    @api.expect(create_update_student_schema)
    def post(self) -> Tuple[Dict[str, Any], int]:
        """Create new Student"""
        session = Session()
        student_repo = StudentRepository(session)
        data = request.get_json()
        student = student_repo.create_student(**data)
        return student.to_dict(), 201

    @api.doc(model=get_student_schema)
    @api.expect(create_update_student_schema)
    def put(self, student_id) -> Tuple[Union[Dict[str, Any], Dict[str, str]], int]:
        """Update Student by ID"""
        session = Session()
        student_repo = StudentRepository(session)
        data = request.get_json()
        student = student_repo.update_student(student_id, **data)
        if student:
            return student.to_dict(), 200
        else:
            return {"error": "Student not found"}, 404

    def delete(self, student_id) -> Tuple[Union[Dict[str, Any], Dict[str, str]], int]:
        """Delete Student by ID"""
        session = Session()
        student_repo = StudentRepository(session)
        student = student_repo.delete_student(student_id)
        if student:
            return {"message": "Student removed successfully"}, 200
        else:
            return {"error": "Student not found"}, 404
