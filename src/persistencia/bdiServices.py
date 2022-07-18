from abc import ABC
import os
import mysql.connector
from dotenv import load_dotenv


class BDIAbstract(ABC):
    def __init__(self):
        pass

        """
        Classe abstrata de conexão com o banco de dados. 
        """
    @property
    def host(self):
        return self.__host

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def db(self):
        return self.__db

    def connect(self):
        pass

    def execute(self, query, parameters) -> bool:
        pass

    def get_one(self, query, parameters) -> dict:
        pass

    def get_all(self, query, parameters) -> list:
        pass


class MySQLConnection(BDIAbstract):
    def __init__(self):
        super().__init__()
        self.cnx = None
        
        """
        Classe para se conectar com o MySQL. 

        """

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD"),
                host=os.getenv("HOST"),
                database=os.getenv("NAME"),
            )
        except mysql.connector.Error as err:
            print(err)
            return False
        return True


    def execute(self, query:str, parameters):
        try:
            if not self.connect():
                return False
            cursor = self.cnx.cursor()                 
            cursor.execute(query.replace('?', '%s'), tuple(parameters))
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
        except Exception as e:
            print(e)
            return False
        return True


    def get_one(self, query:str, parameters) -> dict:
        try:
            if not self.connect():
                return False
            cursor = self.cnx.cursor()
            cursor.execute(query.replace('?', '%s'), tuple(parameters))
            resultado = cursor.fetchone()
            cursor.close()
            self.cnx.close()
        except Exception as e:
            print(e)
            return None
        return resultado


    def get_all(self, query:str, parameters) -> list:
        try:
            if not self.connect():
                return False
            cursor = self.cnx.cursor()
            cursor.execute(query.replace('?', '%s'), tuple(parameters))
            result = cursor.fetchall()
            cursor.close()
            self.cnx.close()
        except Exception as e:
            print(e)
            return False
        return result


class SQLiteConnection:
    def __init__(self, conn):
        self.conn = conn

        """
        Classe para se conectar com o SQlite.
        É usado o SQLite em memória para realizar os testes da persistência.
        """

    def execute(self, query:str, parameters):
        cursor = self.conn.cursor()
        cursor.execute(query, parameters)
        self.conn.commit()
        cursor.close()


    def get_one(self, query, parameters) -> dict:
        cursor = self.conn.cursor()
        cursor.execute(query, parameters)
        resultado = cursor.fetchone()
        cursor.close()
        return resultado


    def get_all(self, query, parameters) -> list:
        cursor = self.conn.cursor()
        cursor.execute(query, parameters)
        result = cursor.fetchall()
        cursor.close()
        return result
