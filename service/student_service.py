from dao.impl.student_dao import StudentDao


class StudentService:
    """
    define basic student method, including:

    Fields:
        _student_dao refers to the student data access, it provides CRUD operations with Student Basic information

    Methods:
        _init:              public default constructor, init _student_dao object

        login:              public method for login (get login info from keyboard)
        register:           public method for register new student (get key information from keyboard)
        change_password     public method for change student's password

    """

    def __init__(self):
        # init _student_dao by using default constructor of StudentDao
        self._student_dao = StudentDao()

    def login(self) -> bool:
        """
        perform login process

        :param email:       student's email used as parameter to query from data file and fetch a student object.
        :param password:    student's password used for comparison if the input parameter is the same as it in database.
        :return: Student:   if student login successfully, return student object, otherwise None
        """
        print("Student Log in")
        # 1: get email and password from keyboard
        # email = str(input("Email: "))
        # password = str(input("Password: "))

        # 2: check email and password pattern by calling Util.check_pattern
        # check_ret = Util.check_pattern(email, password)
        # if not check_ret:
        #     pass

        # 3: query student basic information by using student_name by calling _student_dao.query_student_by_email
        # TODO

        # 4: encode password of parameter, and then compare the encryption
        # TODO

        # 5: upon logining, assign student entity to field: _student
        # TODO

        return False

    def register(self) -> bool:
        """
        register by using username, email and password.
        :param name:        student's name, must be unique
        :param email:       student's email, must be unique
        :param password:    student's password, for safety, please encode it with MD5 or something like that.
        :return: None
        """

        print("Student Sign Up")
        # 1: get email and password from keyboard
        # email = str(input("Email: "))
        # password = str(input("Password: "))
        # name = str(input("Name: "))

        # 2: check email and password pattern by calling Util.check_pattern
        # check_ret = Util.check_pattern(email, password)
        # if not check_ret:
        #     return False

        # 3: check whether student is existed or not ( eq: check if the email is exist )
        #      should invoke _student_dao.query_student_by_email to check whether the input email is exist.
        # TODO

        # 4: build student object
        # 4.1: using student's constructor with parameters of student_id, student_name, student_email, student_password
        #   **Note** DO NOT need to pass by student_category and subject_list
        #            due to system automatically assigned to with a separate process
        # 4.2: generate a encryption for password
        # TODO

        # 5: invoking _student_dao.add_student to saving a new student.
        # TODO

        return False

    def change_password(self) -> bool:
        """
        used for customer to modify their password.

        :return: None
        """

        # 1: query student entity by email.
        #    call _student_dao.query_student_by_email
        # TODO

        # 2: check whether new_password meet the pattern requirement.
        # TODO

        # 3: check whether old_password equals exist password.
        #    encode password of parameter, and then compare the encryption
        #    call @Util.encode_md5 to get encrypted string
        # TODO

        # 4: update data to database file
        #    call _student_dao.update_student
        pass
