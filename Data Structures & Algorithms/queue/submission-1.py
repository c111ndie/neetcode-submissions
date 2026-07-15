class ListNode:

    def __init__(self, val = 0):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return not self.head 

    def append(self, value: int) -> None:
        newNode = ListNode(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        n = self.tail.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return n
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return n

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        n = self.head.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return n
        self.head.next.prev = None
        self.head = self.head.next
        return n
