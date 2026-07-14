class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index):
            if cur == None:
                return -1
            cur = cur.next
        if cur == None:
            return -1
        return cur.val

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode 
        

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head and self.head is self.tail:
                self.head = None
                self.tail = None
                return True
            elif not self.head:
                return False
            else:
                self.head = self.head.next
                return True
        cur = self.head
        for i in range(index - 1):
            if cur == None:
                return False
            cur = cur.next
        if cur is None or cur.next is None:
            return False  
        elif cur.next == None:
            return False
        else:
            if cur.next == self.tail:
                self.tail = cur
                cur.next = None
                return True
            else:
                cur.next = cur.next.next
                return True

    def getValues(self) -> List[int]:
        if self.head is None:
            return []
        values = []
        cur = self.head
        while cur != self.tail:
            values.append(cur.val)
            cur = cur.next
        values.append(cur.val)
        return values
