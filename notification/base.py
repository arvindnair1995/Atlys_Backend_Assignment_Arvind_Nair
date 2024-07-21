from abc import ABC, abstractmethod
from typing import Dict, List


class BaseNotification(ABC):
    @abstractmethod
    def notify(self, message: str, products: List[Dict]):
        pass
