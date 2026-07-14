class ListNode:
    
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index == 0:
            if self.head:
                return self.head.val
            else:
                return -1
        cur = self.head
        for i in range(index):
            if cur == None:
                return -1
            cur = cur.next
        if cur == None:
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode


    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            if self.head:
                newNode = ListNode(val)
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
                return
            else:
                return
        cur = self.head
        for i in range(index):
            if cur == None:
                return
            cur = cur.next
        newNode = ListNode(val)
        if cur == None:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            return
        else:
            cur.prev.next = newNode
            newNode.prev = cur.prev
            cur.prev = newNode
            newNode.next = cur
            return


    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head.next = None
                return
            else:
                return
        cur = self.head
        for i in range(index):
            if cur == None:
                return
            cur = cur.next
        if cur == None:
            return
        elif cur == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.prev = None
            cur.next = None
            return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)