# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_kth(self, cur, k):
        i = 0
        while cur and i < k:
            cur = cur.next
            i += 1
        return cur
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.get_kth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev = groupNext
            cur = groupPrev.next
            for i in range(k):
                nxt = cur.next
                cur.next = prev
                prev, cur = cur, nxt
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
