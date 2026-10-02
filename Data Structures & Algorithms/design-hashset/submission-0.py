class Node:

    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.cap = 1000
        self.array = [None] * self.cap

    def add(self, key: int) -> None:
        idx = key % self.cap
        if not self.array[idx]:
            self.array[idx] = Node(key)
        else:
            cur = self.array[idx]
            while True:
                if cur.key == key:
                    return
                if not cur.next:
                    break
                cur = cur.next
            cur.next = Node(key)

    def remove(self, key: int) -> None:
        idx = key % self.cap
        if not self.array[idx]:
            return
        prev = None
        cur = self.array[idx]
        while True:
            if cur.key == key: 
                if not prev:
                    self.array[idx] = cur.next
                else:
                    prev.next = cur.next
            if cur.next == None:
                return
            prev = cur
            cur = cur.next
            

    def contains(self, key: int) -> bool:
        idx = key % self.cap
        if not self.array[idx]:
            return False
        cur = self.array[idx]
        while True:
            if cur.key == key: 
                return True
            if cur.next == None:
                return False
            cur = cur.next
            


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)