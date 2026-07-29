class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}

    def get(self, key: int) -> int:
        if key in self.lru:
            value = self.lru.pop(key)
            self.lru[key] = value
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            del self.lru[key]
            self.lru[key] = value
        elif len(self.lru) < self.capacity:
            self.lru[key] = value
        else:
            self.lru[key] = self.lru.pop(next(iter(self.lru)))
            self.lru[key] = value

