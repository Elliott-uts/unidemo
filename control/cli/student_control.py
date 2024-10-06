from typing import Dict

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

    def _get_email_password_and_check_pattern(self) -> Dict[str, object]:
        # 1: get email and password from keyboard
        email = str(input("Email: "))
        password = str(input("Password: "))

        # 2: check parameters to find whether they meet the pattern requirements.
        #   please call Util.check_email_pattern to check whether email is valid.
        #   please call Util.check_password_pattern to check whether password is valid
        ret1 = Util.check_email_pattern(email)
        ret2 = Util.check_password_pattern(password)

        # 3 handle exception if any of ret1 and ret2 is false
        if not ret1 or not ret2:
            print("Incorrect email or passport format.")
            return {"is_success": False}
        else:
            print("Email and password formats acceptable.")

        # 4 encapsulate the result with Dict.
        return {"email": email, "password": password, "is_success": True}

    def _register(self) -> None:
        print("Student Sign Up")

        # 1: get username and password from keyboard
        input_map = self._get_email_password_and_check_pattern()
        if not input_map.get("is_success"):
            return

        # 2: get username from keyboard
        name = str(input("Name: "))

        # 4: call student_service.register to register a new student
        self._student_service.register(name, input_map.get("email"), input_map.get("password"))

    def _login(self):
        print("Student Log in")

        # 1: get username and password from keyboard
        input_map = self._get_email_password_and_check_pattern()
        if not input_map.get("is_success"):
            return

        # 2: call _student_service.login to log in for performing further operations
        student = self._student_service.login(input_map.get("email"), input_map.get("password"))
        if not student:
            print("")
        else:
            self._show_student_operation_menu(student)
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
