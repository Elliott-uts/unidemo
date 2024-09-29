class Student:
    """
    Student class
    Declare the attributes and functions in Student

    Fields:
        _student_id
        TODO
    Methods:
        1. must override following 4 methods.
            __init__    for definition a full parameters constructor
            __str__     override for outputting the object to string
            __eq__      override for comparison two object whether they are logically the same.
                        please ensure to use @__hash__ to compare two object value
            __hash__    override for definition hash value for each object, used in __eq__ method
        2. must include traditional setter and getter methods.
            getter      for encapsulate the access to all attributes.
                        **NOTE** for better understanding encapsulation,
                        please use traditional getter, don't use property to define getter
            setter      for encapsulate the modification to all attributes.
                        **NOTE** for better understanding encapsulation,
                        please use traditional getter, don't use property to define getter
    """

    def __init__(self, student_id, subjects):
        # TODO please complete the other attributes
        # _student_id is the unique identifier for each student, exist as primary key in student table.
        self._student_id = student_id

    def get_student_id(self):
        # getter for _student_id
        return self._student_id

    def set_student_id(self, student_id):
        # setter for _student_id
        self._student_id = student_id

    def __eq__(self, __value):
        """
        TODO please
        :param __value:
        :return:
        """
        return ""

    def __str__(self):
        """
        TODO please
        :return:
        """
        return ""

    def __hash__(self):
        """
        TODO please
        :return:
        """
        return ""
