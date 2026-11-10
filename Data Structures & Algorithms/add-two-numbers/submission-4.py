# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            next_carry = (l1.val + l2.val + carry) // 10
            cur.next = ListNode((l1.val + l2.val + carry) % 10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
            carry = next_carry
        if l1:
            while l1:
                next_carry = (l1.val + carry) // 10
                cur.next = ListNode((l1.val + carry) % 10)
                l1 = l1.next
                cur = cur.next
                carry = next_carry
        elif l2:
            while l2:
                next_carry = (l2.val + carry) // 10
                cur.next = ListNode((l2.val + carry) % 10)
                l2 = l2.next
                cur = cur.next
                carry = next_carry
        if carry > 0:
            cur.next = ListNode(int(carry))
        return dummy.next
        