from service.student_service import StudentService
from service.subject_service import SubjectService


class StudentControl:
    """
    student control that just for navigation, menu selection interaction, exception handling, display message.
    **Note** DO NOT type any functional methods in this layer (View or Control layer)

    Fields:
        _student_service: functional service that specified to perform student basic functions.
        _subject_service: functional service that specified to execute subject enrollment functions.

    Methods:
        __init__:                       default constructor that init _student_service and _subject_service
        _show_student_operation_menu:   private method that show student's operational options
        show_student_main_menu:         public method that show student's main options.
    """

    def __init__(self):
        self._student_service = StudentService()
        self._subject_service = SubjectService()

    def show_student_main_menu(self):
        while True:
            try:
                option = str(input("\tStudent System: (l/r/x) : ")).lower()

                # call _student_service.login to log in for performing further operations
                if option == 'l':
                    # upon logining, show student operation menu.
                    if self._student_service.login():
                        self._show_student_operation_menu()
                # call student_service.register to register a new student
                elif option == 'r':
                    self._student_service.register()

                # navigate to University System Menu
                elif option == 'x':
                    break

                # incorrect input, loop continue
                else:
                    raise Exception("Incorrect input, please try again.")
            except Exception as e:
                print(str(e))

    def _show_student_operation_menu(self):
        while True:
            try:
                option = str(input("\tStudent Course Menu: (c/e/r/s/x) : ")).lower()

                # for changing student's password
                # call _student_service.change_password
                if option == 'c':
                    self._student_service.change_password()

                # for subject enrollment
                # call _subject_service.enroll_subject()
                elif option == 'e':
                    self._subject_service.enroll_subject()

                # for removing subject enrollment
                # call _subject_service.remove_subject()
                elif option == 'r':
                    self._subject_service.remove_subject()

                # for showing enrolled subjects
                # call _subject_service.show_subjects()
                elif option == 's':
                    self._subject_service.show_subjects()

                # for navigating to parent menu
                elif option == 'x':
                    break

                # incorrect input, loop continue
                else:
                    raise Exception("Incorrect input, please try again.")
            except Exception as e:
                print(str(e))
