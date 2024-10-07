from typing import List

from dao.entity.student import Student
from dao.impl.abs_dao import AbsDao


class StudentDao(AbsDao):
    def __init__(self):
        super().__init__()

    def add_student(self, student) -> None:
        # TODO
        pass

    def query_student_info_by_id(self, student_id) -> Student:
        # TODO
        pass

    def query_student_list(self) -> List[Student]:
        # TODO
        pass

    def query_student_by_email(self, email) -> Student:
        pass

    def update_student(self, student) -> None:
        pass

    def delete_student_by_id(self, student_id) -> None:
        pass
