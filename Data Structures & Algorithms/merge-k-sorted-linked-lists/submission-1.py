# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        i = 0
        mergedLists = []
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        while i < len(lists):
            if i == len(lists) - 1:
                mergedLists.append(lists[i])
                break
            mergedLists.append(self.mergeTwoLists(lists[i], lists[i+1]))
            i += 2
        return self.mergeKLists(mergedLists)
        
    
    def mergeTwoLists(self, l1, l2):
        dummy = node = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        elif l2:
            node.next = l2
        return dummy.next