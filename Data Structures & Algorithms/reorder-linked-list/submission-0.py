# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        i = head
        while i and i.next:
            j = i.next
            while j.next and j.next.next:
                j = j.next
            if j.next:
                k = i.next
                i.next = j.next
                j.next = None
                i.next.next = k
            i = i.next.next