# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            new = list1
            other = list2
        else:
            new = list2
            other = list1
        cur = new
        while cur.next and other:
            if cur.next.val <= other.val:
                cur = cur.next
            else:
                tmp = cur.next
                cur.next = other
                other = other.next
                cur.next.next = tmp
                cur = cur.next
        if cur.next:
            return new
        else:
            cur.next = other
            return new
