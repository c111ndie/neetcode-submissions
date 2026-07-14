# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == []:
            return list2
        elif list2 == []:
            return list1
        head = ListNode()
        cur = head
        p1 = list1
        p2 = list2
        while p1 != None or p2 != None:
            if p1 and p2:
                if p1.val <= p2.val:
                    newNode = ListNode(p1.val)
                    p1 = p1.next
                else:
                    newNode = ListNode(p2.val)
                    p2 = p2.next
            elif not p1:
                newNode = ListNode(p2.val)
                p2 = p2.next
            else:
                newNode = ListNode(p1.val)
                p1 = p1.next
            cur.next = newNode
            cur = cur.next
        head = head.next
        return head
            