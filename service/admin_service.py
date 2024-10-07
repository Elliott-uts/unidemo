from dao.impl.admin_dao import AdminDao
from service.student_service import StudentService
from service.subject_service import SubjectService


class AdminService:
    """
    define admin service, including:

    Fields:
        _admin_dao refers to the data access, it provides multiple CRUD operations with Student Basic information
            Note: excluding student's enrollment information

    Methods:
        _init:              public default constructor, init _subject_dao object

        enroll_subject      public method for enrollment student's subject
        remove subject      public method for removing one student's subject
        show_subjects       public method for show all subjects enrolled.
    """

    def __init__(self):
        self._admin_dao = AdminDao()
        self._student_service = StudentService()
        self._subject_service = SubjectService()

    def clear_database(self):
        pass

    def group_students(self):
        pass

    def partition_students(self):
        pass

    def remove_student(self):
        pass

    def show_all_students(self):
        pass
