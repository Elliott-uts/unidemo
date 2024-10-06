from dao.entity.student import Student
from dao.impl.student_dao import StudentDao


class StudentService:
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
        self._student = None

    def login(self, email, password) -> None:
        """
        perform login process

        :param email:       student's email used as parameter to query from data file and fetch a student object.
        :param password:    student's password used for comparison if the input parameter is the same as it in database.
        :return: Student:   if student login successfully, return student object, otherwise None
        """
        # 1: query student basic information by using student_name by calling _student_dao.query_student_by_email
        # TODO

        # 2: encode password of parameter, and then compare the encryption


        pass

    def register(self, name, email, password) -> None:
        """
        register by using username, email and password.
        :param name:        student's name, must be unique
        :param email:       student's email, must be unique
        :param password:    student's password, for safety, please encode it with MD5 or something like that.
        :return: None
        """

        # 1: check whether student is existed or not.
        # 1.1: check if the name is exist.
        # 1.2: check if the email is exist.
        # TODO

        # 2: build student object
        # 2.1: using student's constructor with parameters of student_id, student_name, student_email, student_password
        #   **Note** DO NOT need to pass by student_category and subject_list
        #            due to system automatically assigned to with a separate process
        # 2.2: generate a encryption for password
        # TODO

        # 3: invoking _student_dao.add_student to saving a new student.
        # TODO

    def change_password(self, ):
        pass
