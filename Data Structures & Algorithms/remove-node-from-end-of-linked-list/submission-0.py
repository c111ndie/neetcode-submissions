# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        length = 0
        i = head
        while i:
            length += 1
            i = i.next
        delete = length - n
        if delete == 0:
            return head.next
        cur = head
        for _ in range(delete - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head
