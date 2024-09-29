from dao.impl.abs_dao import AbsDao


class StudentDao(AbsDao):
    def __init__(self):
        super().__init__()

    def add_student(self, student):
        pass

    def query_student_info_by_id(self, student_id):
        pass

    def query_student_list(self):
        pass

    def query_student_by_email(self, email):
        pass

    def update_student(self, student):
        pass

    def delete_student_by_id(self, student_id):
        pass
