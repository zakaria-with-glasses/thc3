from HashTable import HashTable

class Bucket(HashTable):
    def __init__(self, size:int = 17) -> None:
        self.size = size
        self.table = [None] * size

        self.hash_result = 0

    def insert(self, key, value) -> bool:

        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key) % self.size
        if self.table[index] is not None:
           probe = self._