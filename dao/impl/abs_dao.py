from dao.database.database import Database


class AbsDao:

    def __init__(self):
        self._database = Database()