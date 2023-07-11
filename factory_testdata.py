import random
import string
from faker import Faker
from src.config import Config
from src.db import create_engine_with_config
from src.db.repository.course_repository import CourseRepository
from src.db.repository.groups_repository import GroupRepository
from src.db.repository.students_repository import StudentRepository


class TestDataFactory:
    def __init__(self, db_config):
        self.engine, self.Session = create_engine_with_config(db_config)
        self.session = self.Session()

    @staticmethod
    def _generate_group_name():
        letters = string.ascii_uppercase
        numbers = string.digits
        group_name = random.choice(letters) + random.choice(letters) + "-" + random.choice(numbers) + random.choice(numbers)
        return group_name

    @staticmethod
    def generate_random_text(max_size):
        fake = Faker("uk_UA")
        return fake.text(max_nb_chars=max_size)

    @staticmethod
    def _generate_student_name():
        fake = Faker("uk_UA")
        return fake.passport_owner()

    @staticmethod
    def _generate_course_name():
        fake = Faker("uk_UA")
        return fake.job()

    def generate_groups(self, count):
        group_repo = GroupRepository(self.session)
        groups = []
        for _ in range(count):
            group_name = self._generate_group_name()
            group = group_repo.create_group(group_name)
            groups.append(group)
        return groups

    def generate_courses(self, count):
        course_repo = CourseRepository(self.session)
        courses = []
        for _ in range(count):
            name = self._generate_course_name()
            description = self.generate_random_text(200)
            course = course_repo.create_course(name, description)
            courses.append(course)
        return courses

    def generate_students(self, count):
        student_repo = StudentRepository(self.session)
        students = []
        for student in range(count):
            student = student_repo.create_student(*self._generate_student_name())
            students.append(student)
        self.session.commit()
        return students


    def assign_students_to_groups(self):
        group_repo = GroupRepository(self.session)
        groups = group_repo.get_all_groups()
        student_repo = StudentRepository(self.session)
        students = student_repo.get_all_students()
        for student in students:
            group = random.choice(groups)
            if not student.group:
                if len(group_repo.get_students_in_group(group.id)) <= 30:
                    group_repo.assign_student_to_group(group.id, student.id)
        self.session.commit()


    def assign_courses_to_students(self):
        course_repo = CourseRepository(self.session)
        courses = course_repo.get_all_courses()
        student_repo = StudentRepository(self.session)
        students = student_repo.get_all_students()
        for student in students:
            count_courses = random.randint(1, 3)
            selected_courses = random.sample(courses, count_courses) if count_courses <= len(courses) else courses
            for course in selected_courses:
                if len(course_repo.get_all_courses_for_student(course.id)) < 3:
                    course_repo.assign_student_to_course(student.id, course.id)
        self.session.commit()


factory = TestDataFactory(Config.development)
groups = factory.generate_groups(40)
courses = factory.generate_courses(300)
students = factory.generate_students(300)
factory.assign_students_to_groups()
factory.assign_courses_to_students()
