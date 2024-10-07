from service.admin_service import AdminService


class AdminControl:
    """
    student control that just for navigation, menu selection interaction, exception handling, display message.
    **Note** DO NOT type any functional methods in this layer (View or Control layer)

    Fields:
        _admin_service:     functional service that specified to query admin basic information.
        _subject_service:   functional service that specified to execute subject enrollment functions.

    Methods:
        __init__:                       default constructor that init _student_service and _subject_service
        _show_student_operation_menu:   private method that show student's operational options
        show_student_main_menu:         public method that show student's main options.
    """

    def __init__(self):
        self._admin_service = AdminService()
        pass

    def show_admin_main_menu(self):
        while True:
            try:
                option = str(input("\tAdmin System: (c/g/p/r/s/x) : ")).lower()

                # call _admin_service.clear_database to delete all student's information and enrollment records.
                if option == 'c':
                    self._admin_service.clear_database()

                # call _admin_service.group_students to show students by grade
                elif option == 'g':
                    self._admin_service.group_students()

                # call _admin_service.partition_students to partition students to PASS/FAIL categories.
                elif option == 'p':
                    self._admin_service.partition_students()

                # call _admin_service.remove_student to remove student by id.
                elif option == 'r':
                    self._admin_service.remove_student()

                # call _admin_service.show_all_students to show all student's and enrollment information.
                elif option == 's':
                    self._admin_service.show_all_students()

                # navigate to University System Menu
                elif option == 'x':
                    break

                # incorrect input, loop continue
                else:
                    raise Exception("Incorrect input, please try again.")
            except Exception as e:
                print(str(e))
