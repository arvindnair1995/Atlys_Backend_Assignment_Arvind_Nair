from typing import Dict

from pysondb import db

from core.config import DATABASE
from repository.base import BaseRepository


class PysondbRepository(BaseRepository):

    def __init__(self):
        self.db = db.getDb(DATABASE)


    def add_product(self, product: Dict):
        self.db.add(product)


    def get_products_size(self) -> int:
        return len(self.db.getAll())
    

    def is_product_present_in_DB(self, title) -> bool:
        if len(self.db.getBy({"product_title": title})):
            return True
        else:
            return False

