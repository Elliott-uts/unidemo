from dao.impl.enrollment_dao import EnrollmentDao
from dao.impl.student_dao import StudentDao


class StudentMgtService:
    def __init__(self):
        self._student_dao = StudentDao()
        self._enrollment_dao = EnrollmentDao()

    def delete_student_by_id(self, student_id):
        pass

    def delete_all_students(self):
        pass

