from typing import List

from dao.impl.abs_dao import AbsDao
from dao.entity.enrollment import Enrollment


class EnrollmentDao(AbsDao):

    def __init__(self):
        super().__init__()

    def add_enrollment(self, enrollment):
        pass

    def query_enrollment_list_by_student_id(self, student_id) -> List[Enrollment]:
        pass

    def query_enrollment_by_student_and_subject(self, student_id, subject_id) -> Enrollment:
        pass

    def query_enrollment_list_by_subject_id(self, subject_id) -> List[Enrollment]:
        pass

    def count_enrollment_by_student_id(self, student_id) -> int:
        pass

    def delete_enrollment_by_student_and_subject(self, student_id, subject_id):
        pass

    def delete_enrollment_list_by_student_id(self, student_id):
        pass

    def update_enrollment(self, enrollment):
        pass
