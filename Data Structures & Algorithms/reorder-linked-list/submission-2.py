# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        list1, list2 = head, prev
        while list2:
            tmp1 = list1.next
            list1.next = list2
            tmp2 = list2.next
            list1.next.next = tmp1
            list1 = tmp1
            list2 = tmp2