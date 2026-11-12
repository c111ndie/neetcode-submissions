# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        tail = dummy
        node = head
        while node:
            check = node
            for _ in range(k):
                if not check:
                    return dummy.next
                else:
                    check = check.next
            newHead, nextReverse = self.reverseList(node, k)
            tail.next = newHead
            node.next = nextReverse
            tail = node
            node = nextReverse
            
        return dummy.next
            
        
    def reverseList(self, head, k):
        i = 0
        prev, cur = None, head
        while cur and i < k:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            i += 1
        return (prev, cur)
        