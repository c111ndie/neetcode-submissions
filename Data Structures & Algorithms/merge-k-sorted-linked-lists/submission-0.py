# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0)
        cur = dummy

        while True:
            clean_map = {
                i: node
                for i, node in enumerate(lists)
                if node is not None
            }

            if not clean_map:
                break

            min_key = min(clean_map, key=lambda k: clean_map[k].val)

            cur.next = lists[min_key]
            cur = cur.next
            lists[min_key] = lists[min_key].next

        return dummy.next