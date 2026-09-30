class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev, self.next = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {} # map key to node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            val = node.value
            self.remove(node)
            self.insert(node)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.lru) < self.capacity:
            if key in self.lru:
                self.remove(self.lru[key])
        else:
            if key in self.lru:
                self.remove(self.lru[key])
            else:
                oldest = self.left.next
                self.lru.pop(oldest.key)
                self.remove(oldest)
        node = Node(key, value)
        self.insert(node)
        self.lru[key] = node
            
        
