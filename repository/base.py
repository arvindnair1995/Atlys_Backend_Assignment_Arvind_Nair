from abc import ABC, abstractmethod
from typing import Dict, List


class BaseRepository(ABC):

    @abstractmethod
    def add_product(self, product: Dict):
        pass


    @abstractmethod
    def add_many_products(self, products: List[Dict]):
        pass


    @abstractmethod
    def get_products_size(self) -> int:
        pass


    @abstractmethod
    def get_product_price(self, title: str) -> int:
        pass
