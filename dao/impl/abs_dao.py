from dao.database.database import Database


class AbsDao:
    """
    Define an abstract class as super class to all other dao class.
    Providing a common field: _database that includes all data file operations.
    """
    def __init__(self):
        self._database = Database()
