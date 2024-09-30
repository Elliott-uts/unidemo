from dao.impl.subject_dao import SubjectDao
from dao.impl.student_dao import StudentDao


class StudentMgtService:
    def __init__(self):
        self._student_dao = StudentDao()
        self._enrollment_dao = SubjectDao()

    def delete_student_by_id(self, student_id):
        pass

    def delete_all_students(self):
        pass

