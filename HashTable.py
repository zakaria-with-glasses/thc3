from abc import ABC, abstractmethod
from typing import TypeVar
T = TypeVar('T')
class HashTable(ABC):

    @abstractmethod
    def insert(self, key:int, value:T) -> bool:
        """Insert a key-value pair into the hash table."""
        pass

    @abstractmethod
    def remove(self, key) -> T:
        """Remove a key-value pair from the hash table."""
        pass

    @abstractmethod
    def search(self, key) -> bool:
        """Search for a value by key in the hash table."""
        pass