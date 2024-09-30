from service.student_service import StudentService
from util.util import Util


class StudentControl:

    """
    student control that just for navigation, menu selection, and exception handling.
    **Note** DO NOT type any functional methods in this layer (View or Control layer)

    Fields:
        _student_service: functional service that specified to perform student basic functions.

    Methods:
        _register:          private method that getting input values of email and password,
                            then call student service to register and handle optional exceptions
        _login:             private method that getting input values of email and password,
                            then call student service to log in, and handle optional exceptions.
        _change_password:   private method that getting new password from keyboard,
                            then call student service to change password and handle optional exceptions

        show_student_menu:  public method that show student operation options.
    """

    def __init__(self):
        self._student_service = StudentService()

    def _get_email_password_and_check_pattern(self) -> Map:
        # 1: get email and password from keyboard
        print("Student Sign Up")
        email = str(input("Email: "))
        password = str(input("Password: "))

        # 2: check parameters to find whether they meet the pattern requirements.
        #   please call Util.check_email_pattern to check whether email is valid.
        #   please call Util.check_password_pattern to check whether password is valid
        # TODO
        return ""

    def _register(self) -> None:

        # 3: get username from keyboard
        name = str(input("Name: "))

        # 4: call student_service.register to register a new student
        # self._student_service.register(name, email, password)

    def _login(self):
        # 1: get password
        print("Student Sign Up")
        email = str(input("Email: "))
        password = str(input("Password: "))
        pass

    def show_student_menu(self):
        while True:
            option = str(input("\tStudent System: (l/r/x) : ")).lower()

            # call private register method
            if option == 'l':
                self._login()

            # show student menu
            elif option == 'r':
                self._register()

            # navigate to University System Menu
            elif option == 'x':
                print()
                break

            # incorrect input, loop continue
            else:
                print("Incorrect input, please try again.")
