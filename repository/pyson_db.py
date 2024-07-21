from typing import Dict, List

from pysondb import db

from core.config import DATABASE
from repository.base import BaseRepository


class PysondbRepository(BaseRepository):

    def __init__(self):
        self.db =  db.getDb(DATABASE)


    def add_product(self, product: Dict):
        self.db.add(product)


    def add_many_products(self, products: List[Dict]):
        self.db.addMany(products)


    def get_products_size(self) -> float:
        return len(self.db.getAll())
    

    def get_product_price(self, title: str) -> float:
        product = self.db.getBy({"product_title": title})
        if len(product) == 1:
            return product[0]['product_price']
        else:
            return -1

