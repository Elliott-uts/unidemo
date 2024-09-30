from dao.impl.student_dao import StudentDao


class StudentBasicService:
    """
    define basic student method, including:

    Fields:
        _student_dao refers to the data access, it provides multiple CRUD operations with Student Basic information
            Note: excluding student's enrollment information

    Methods:


    """
    def __init__(self):
        # init _student_dao by using default constructor of StudentDao
        self._student_dao = StudentDao()

    def login(self, email, password):
        """

        :param email:
        :param password:
        :return:
        """
        pass

    def register(self, username, email, password):
        """
        register by using username, email and password.
        step 1: these three parameters must be meet the pattern requirements.
                please call Util.check_username_pattern to check whether username is valid
                please call Util.check_email_pattern to check whether email is valid
                please call Util.check_password_pattern to check whether password is valid
        step 2: check whether student is existed or not.
        step 3: build student object and save to database
                using student's constructor with full parameters.
                invoking _student_dao.add_student to saving a new student.

        :param username: student's username,
        :param email:
        :param password:
        :return: void
        """

        # TODO
        pass

    def change_password(self, ):
        pass


