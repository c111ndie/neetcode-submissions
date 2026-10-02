class Node:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.cap = 1000
        self.array = [None] * self.cap

    def put(self, key: int, value: int) -> None:
        idx = key % self.cap
        if self.array[idx]:
            cur = self.array[idx]
            while True:
                if cur.key == key:
                    cur.val = value
                    return
                if cur.next is None:
                    cur.next = Node(key, value)
                    return
                cur = cur.next
        else:
            self.array[idx] = Node(key, value)

    def get(self, key: int) -> int:
        idx = key % self.cap
        cur = self.array[idx]
        while cur and cur.key != key:
            cur = cur.next
        if cur:
            return cur.val
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.cap
        if self.array[idx]:
            prev = None
            cur = self.array[idx]
            while cur and cur.key != key:
                prev = cur
                cur = cur.next
            if cur:
                if prev:
                    prev.next = cur.next
                else:
                    self.array[idx] = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)