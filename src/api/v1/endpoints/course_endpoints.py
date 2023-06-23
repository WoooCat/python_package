from typing import Any, Dict, List, Tuple, Union

from flask import request
from flask_restx import Resource

from src.api_utils import api
from src.db import Session
from src.db.repository.course_repository import CourseRepository
from src.schemas.cource_schemas import create_course_schema, get_course_schema


class CoursesResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.doc(model=get_course_schema)
    def get(self) -> Tuple[Union[Dict[str, Any], Tuple[List[Dict[str, Any]], int]], int]:
        """Get all Courses"""
        session = Session()
        course_repo = CourseRepository(session)
        courses = course_repo.get_all_courses()
        return {"courses": [course.to_dict() for course in courses]}, 200


class CourseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.doc(model=get_course_schema)
    def get(self, course_id: int) -> Tuple[Union[Dict[str, Any], Tuple[List[Dict[str, Any]], int]], int]:
        """Get Course by ID"""
        session = Session()
        course_repo = CourseRepository(session)
        course = course_repo.get_course_by_id(course_id)
        if course:
            return course.to_dict(), 200
        else:
            return {"error": "Course not found"}, 404

    @api.doc(model=get_course_schema)
    @api.expect(create_course_schema)
    def post(self) -> Tuple[Dict[str, Any], int]:
        """Create new Course"""
        session = Session()
        course_repo = CourseRepository(session)
        data = request.get_json()
        group = course_repo.create_course(**data)
        return group.to_dict(), 201

    @api.doc(model=get_course_schema)
    @api.expect(create_course_schema)
    def put(self, course_id: int = None) -> Tuple[Union[Dict[str, Any], Dict[str, str]], int]:
        """Update Course by ID"""
        session = Session()
        course_repo = CourseRepository(session)
        data = request.get_json()
        course = course_repo.update_course(course_id=course_id, **data)
        if course:
            return course.to_dict(), 200
        else:
            return {"error": "Course not found"}, 404

    def delete(self, course_id: int) -> Tuple[Union[Dict[str, Any], Dict[str, str]], int]:
        """Delete Course by ID"""
        session = Session()
        course_repo = CourseRepository(session)
        course = course_repo.delete_course(course_id)
        if course:
            return {"message": "Course deleted successfully", "course_id": course.id}, 200
        else:
            return {"error": "Course not found"}, 404


class CourseStudentResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def put(self, course_id: int, student_id: int) -> Tuple[Dict[str, str], int]:
        """Assign Student to Course"""
        session = Session()
        course_repository = CourseRepository(session)
        course_student = course_repository.assign_student_to_course(course_id, student_id)
        if course_student:
            return {"message": f"Student with id: {student_id} successfully added to the Course"}, 200
        else:
            return {"message": f"Course with id: '{course_id}' or Student with id: '{student_id}' not found"}, 404

    def patch(self, course_id: int, student_id: int) -> Tuple[Dict[str, str], int]:
        """Remove Student from Course"""
        session = Session()
        course_repository = CourseRepository(session)
        course_student = course_repository.remove_student_from_course(course_id, student_id)
        if course_student:
            return {"message": f"Student with id: {student_id} successfully removed from Course"}, 200
        else:
            return {"message": f"Course with id: '{course_id}' or Student with id: '{student_id}' not found"}, 404
