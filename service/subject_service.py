from dao.impl.subject_dao import SubjectDao


class SubjectService:
    """
    define basic student method, including:

    Fields:
        _subject_dao refers to the subject data access, it provides CRUD operations with Subject enrollment information

    Methods:
        _init:              public default constructor, init _subject_dao object

        enroll_subject      public method for enrollment student's subject
        remove subject      public method for removing one student's subject
        show_subjects       public method for show all subjects enrolled.
    """

    def __init__(self):
        self._subject_dao = SubjectDao()

    def enroll_subject(self):
        """

        :return:
        """
        # 1:
        pass

    def remove_subject(self):
        pass

    def show_subjects(self):
        pass
