from mysql.connector import Error
from unittest import TestCase
from src.persistencia.bdiServices import MySQLConnection


class TestDB(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.db = MySQLConnection

    def test_connect_db(self):
        try:
            cnx = self.db.connect(self)
            result = True
        except Error as err:
            cnx.close()
            return result==False
        
        self.assertTrue(result)
