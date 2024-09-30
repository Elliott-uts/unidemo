from dao.impl.abs_dao import AbsDao


class AdminDao(AbsDao):

    def __init__(self):
        super().__init__()

    def query_admin_by_staff_id(self, staff_id):
        """
        reserved method, don't need to implement.
        :param staff_id:  staff_id
        :return: Admin
        """
        pass

    def query_admin_by_staff_name(self, staff_name):
        """
        reserved method, don't need to implement.
        :param staff_name: staff name
        :return: Admin
        """
        pass
