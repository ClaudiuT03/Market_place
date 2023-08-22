"""
DB CRUD methods for Orders table
"""
from crud.interface_crud import CrudABC


class Orders(CrudABC):

    def create(self, entry_to_create):
        pass

    def read(self, id=None):
        pass

    def update(self, entry_for_update):
        pass

    def delete(self, id):
        pass
