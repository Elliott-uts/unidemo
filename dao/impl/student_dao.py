from typing import List

from dao.entity.student import Student
from dao.impl.abs_dao import AbsDao


class StudentDao(AbsDao):
    """
    Student Data Access Object
    providing CRUD operations of student information
        add_student:                add a new student into database
        query_student_info_by_id:   get a specific student by using student_id
        query_student_list:         get a student list which includes all student information
        query_student_by_email:     get a specific student by using student_email
        update_student:             update a student's information and save to the database
        delete_student_by_id:       delete a student and all enrollments by student_id

    ** Note ** About Data Integrity:
        ->  Service layer is responsible for Data integrity, logically.
        ->  Dao layer just for CURD. don't check any data integrity
    """

    def __init__(self):
        # init database instance
        super().__init__()

    def add_student(self, student):
        """
        Add a new student information to database

        :param      student: student information, excluding _student_category and _subject_list
        :return:    return none if process succeed
        """
        # 1: query students list
        students = self._database.get_students()

        # 2: check for none and duplicate entity
        if students:
            students.append(student)
            # check duplicate entity
            # matching_id = [item for item in students if (item.get_student_id() == student.get_student_id())]
            # matching_name = [item for item in students if (item.get_student_name() == student.get_student_name())]
            # matching_email = [item for item in students if (item.get_student_email() == student.get_student_email())]
            #
            # if matching_id:
            #     raise Exception("Student id already exists.")
            # elif matching_name:
            #     raise Exception("Student " + student.get_student_name() + " already exists.")
            # elif matching_email:
            #     raise Exception("Student " + student.get_student_email() + " already exists.")
            # else:
            #     students.append(student)
        else:
            students = [student]

        # 3: saving data to file
        self._database.write_students(students)

    def query_student_info_by_id(self, student_id) -> Student | None:
        """
        Query one student information by using a specific student id

        :param      student_id:     student's id, primary key in database
        :return:    Student or None(if there is no entity is related to parameter)
        """
        # 1: query all student
        students = self._database.get_students()
        # check if students list is empty
        if not students:
            return None

        # 2: filter student
        matching_students = [student for student in students if student.get_student_id() == student_id]

        return matching_students[0] if matching_students else None

    def query_student_by_email(self, email) -> Student | None:
        """
        Query one student information by using a specific student email

        :param      email:     student's email, unique key in database
        :return:    Student or None(if there is no entity is related to parameter)
        """
        # 1: query all student
        students = self._database.get_students()
        # check if students list is empty
        if not students:
            return None

        # 2: filter student
        matching_students = [student for student in students if student.get_student_email() == email]

        return matching_students[0] if matching_students else None

    def query_student_list(self) -> List[Student]:
        """
        query all students
        :return: List[Student]
        """
        students = self._database.get_students()
        return students if students else []

    def update_student(self, student):
        """
        update a student information by given student from parameter
        using delete first add after to simulate update.

        :param student: student information, student_id must be included
        """
        # 1: query student
        students = self._database.get_students()

        # 2: remove student that should be deleted
        remain_students = [item for item in students if item.get_student_id() != student.get_student_id()]

        # 3: add new student that should be added
        remain_students.append(student)

        # 4: saving data to database
        self._database.write_students(remain_students)

    def delete_student_by_id(self, student_id):
        """
        delete one student by using student id

        :param      student_id: student's id, primary key in database
        :exception
        """
        # 1: query all student
        students = self._database.get_students()
        # check if students list is empty
        if not students:
            return

        # 2: filter student to deleting the data that needs to be deleted
        remain_students = [student for student in students if student.get_student_id() != student_id]

        # 3: saving remain students to database
        self._database.write_students(remain_students)
