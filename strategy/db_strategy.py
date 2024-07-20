from abc import ABC, abstractmethod
from pysondb import db
from core.config import DATABASE

class DbStrategy(ABC):
    @abstractmethod
    def setup(self):
        pass

class PysonDBStrategy(DbStrategy):
    def setup(self):
        db.getDb(DATABASE)