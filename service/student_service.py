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

    def login(self, email, password):
        """

        :param email:
        :param password:
        :return:
        """
        pass

    def register(self, name, email, password) -> None:
        """
        register by using username, email and password.
        :param name
        :param email:   emails should end with the domain “@university.com”,
                        hence firstname.lastname@university.com is a valid email,
                        while firstname.lastname@university is not
        :param password:    A password is considered valid if it meets the following criteria:
                            (i) It starts with an upper-case character,
                            (ii) It contains at least five (5) letters,
                            (iii) It is followed by three (3) or more digits.
        :return: None
        """

        # 1: check whether student is existed or not.
        # TODO

        # 2: build student object
        #   using student's constructor with parameters of student_id, student_name, student_email, student_password
        #   DO NOT need to pass by student_category and subject_list
        #   due to system automatically assigned to with a separate process
        # TODO

        # 3: invoking _student_dao.add_student to saving a new student.
        # TODO

    def change_password(self, ):
        pass
