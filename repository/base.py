from abc import ABC, abstractmethod
from typing import Dict

class BaseRepository(ABC):

    @abstractmethod
    def add_product(self, product: Dict):
        pass

    @abstractmethod
    def get_products_size(self) -> int:
        pass

    @abstractmethod
    def is_product_present_in_DB(self, title: str) -> bool:
        pass
