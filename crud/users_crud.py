"""
DB CRUD methods for Users table
"""
from crud.interface_crud import CrudABC


class Users(CrudABC):

    def create(self, entry_to_create):
        SQL_QUERY = """
        INSERT INTO Users(id, username, password, email, is_logged) VALUES (:id, :username, :password, :email, :is_logged)
        """
        cursor = self.connection.cursor()
        cursor.execute(
            SQL_QUERY,
            entry_to_create.__dict__
        )
        self.connection.commit()

    def read(self, id=None):
        SQL_QUERY = """
        SELECT * FROM USERS;
        """
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY)
        self.connection.commit()

        users = cursor.fetchall() # o lista cu liste

        users_json = []
        for user in users:
            users_json.append({
                "id": user[0],
                "username": user[1],
                "password": user[2],
                "email": user[3],
                "is_logged": user[4]
            })
        return users_json

    def update(self, entry_for_update):
        pass

    def delete(self, id):
        pass
