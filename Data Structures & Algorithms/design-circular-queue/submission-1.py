class Node:

    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularQueue: 

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.head = Node()
        cur = self.head
        for _ in range(k-1):
            cur.next = Node()
            cur.next.prev = cur
            cur = cur.next
        self.tail = cur
        self.head.prev = self.tail
        self.tail.next = self.head
        self.cur = self.head

    def enQueue(self, value: int) -> bool:
        if self.size < self.cap:
            self.cur.val = value
            self.cur = self.cur.next
            self.size += 1
            return True
        return False
    def deQueue(self) -> bool:
        if self.size > 0:
            self.head.val = None
            self.head, self.tail = self.head.next, self.head
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        if self.size > 0:
            return self.head.val
        return -1

    def Rear(self) -> int:
        if self.size > 0:
            return self.cur.prev.val
        return -1
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()