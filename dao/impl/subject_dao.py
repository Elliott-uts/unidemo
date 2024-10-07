from typing import List

from dao.impl.abs_dao import AbsDao
from dao.entity.subject import Subject


class SubjectDao(AbsDao):

    def __init__(self):
        super().__init__()

    def add_subject(self, subject):
        # TODO
        pass

    def query_subject_list_by_student_id(self, student_id) -> List[Subject]:
        # TODO
        pass

    def query_subject_by_student_and_subject(self, student_id, subject_id) -> Subject:
        # TODO
        pass

    def delete_subject_by_student_and_subject(self, student_id, subject_id):
        # TODO
        pass

    def delete_subject_list_by_student_id(self, student_id):
        # TODO
        pass

    def update_subject(self, subject):
        # TODO
        pass
