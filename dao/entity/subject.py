class Subject:
    """
    Subject class
    Declare the attributes and functions in Subject

    Fields:
        _subject_id
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

    def __init__(self, subject_id):
        # TODO please complete the other attributes
        # _subject_id is the unique identifier for each subject, exist as primary key in subject table.
        self._subject_id = subject_id

    def get_subject_id(self):
        # getter of _subject_id
        return self._subject_id

    def set_subject_id(self, subject_id):
        # setter of _subject_id
        self._subject_id = subject_id

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





