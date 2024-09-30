from util.util import Util


class Database:
    """
    this is a simulation of database basis operations that include query from file and write data to file.
    Methods:
        __init__: default constructor that init 3 attributes for objects storage:
            _students, _admins, _subjects
            **Note**:   @_init_file() should be called to physically init a file in disk.

        get_students: public method for getting all students basic information.
        get_admins: public method for getting all admins basic information.
        get_subjects: public method for getting all subjects information.
        **Note**:   @_load_file() should be called to load data from data file in disk in all getter methods.

        set_students: public method for saving students information to database file.
        set_admins: public method for saving admins information to database file.
        set_subjects: public method for saving a student's all subjects information to database file.
        **Note**:   @_load_file() should be called to load data from data file in disk in all getter methods.
                    @_overwrite_data should be called to physically saving data to data file in disk.

    """

    def __init__(self):
        """
        step 1: define 4 attributes parsed from student.data file
        """
        # _students array, show all students information
        self._students = []
        # _admins array includes all admins information
        self._admins = []
        # _enrollments array includes all students subject enrollments information
        self._subjects = []

        """
        step 2: state the file path as static and then init the file if file is not exist.
        """
        # 2.1 declare the file's static path.
        self._data_file_path = ""
        # 2.2 init file if it is not exist.
        self._init_file()

    def get_students(self):
        # getter for _students
        self._load_data()
        return self._students

    def get_admins(self):
        # getter for _admins
        self._load_data()
        return self._admins

    def get_subjects(self):
        # getter for _subjects
        self._load_data()
        return self._subjects

    def write_students(self, students):
        # setter for _students

        # 1. load latest data
        self._load_data()

        # 2. process data
        self._students = students

        # 3 call overwrite method for saving data to file
        self._overwrite_data()

    def write_admins(self, admins):
        # setter for _admins
        # 1. load latest data
        self._load_data()

        # 2. process data
        self._admins = admins

        # 3 call overwrite method for saving data to file
        self._overwrite_data()

    def write_subjects(self, subjects):
        # setter for _subjects
        # 1. load latest data
        self._load_data()

        # 2. process data
        self._subjects = subjects

        # 3 call overwrite method for saving data to file
        self._overwrite_data()

    def _load_data(self):
        # load data from file using JSON tools

        # step 1: load all data from student.data by using _data_file_path
        # TODO

        # step 2: parse json string to objects (students array, admin array, subject array, enrollment array)
        # TODO

        # step 3: assign temp objects to attributes.
        # TODO

        pass

    def _overwrite_data(self):
        # overwrite all data to student.data file

        # step 1: format objects to json string
        json_str = Util.object_to_json([self._students, self._admins, self._enrollments, self._subjects])

        # step 2: TODO
        pass

    def _init_file(self):
        # if file is not exist, init the file.
        # TODO
        pass
