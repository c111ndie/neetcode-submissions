class Node:

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.lru = {}

    def insert(self, node):
        prev = self.tail.prev
        self.tail.prev = prev.next = node
        node.prev, node.next = prev, self.tail

    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.lru:
            self.delete(self.lru[key])
            self.insert(self.lru[key])
            return self.lru[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.delete(self.lru[key])
        new = Node(key, value)
        self.lru[key] = new
        self.insert(new)

        if len(self.lru) > self.cap:
            del self.lru[self.head.next.key]
            self.delete(self.head.next)
        
