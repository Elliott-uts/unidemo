class Admin:
    """
    Admin class
    Declare the attributes and functions in Admin

    Fields:
        _staff_id
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

    def __init__(self, staff_id):
        # TODO please complete the other attributes
        # _staff_id is the unique identifier for each staff, exist as primary key of admin table
        self._staff_id = staff_id

    def get_staff_id(self):
        # getter for staff_id
        return self._staff_id

    def set_staff_id(self, staff_id):
        # setter for staff_id
        self._staff_id = staff_id

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





