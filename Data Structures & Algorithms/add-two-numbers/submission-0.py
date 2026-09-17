# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        old_carry = 0
        head = ListNode()
        dummy = head
        while l1 and l2:
            add = l1.val + l2.val + old_carry
            new_carry = add // 10
            add = add % 10
            dummy.next = ListNode(add)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
            old_carry = new_carry
        rest = l1 if l1 else l2
        while rest:
            add = rest.val + old_carry
            new_carry = add // 10
            add = add % 10
            dummy.next = ListNode(add)
            dummy = dummy.next
            rest = rest.next
            old_carry = new_carry
        if old_carry > 0:
            dummy.next = ListNode(old_carry)
        return head.next

        