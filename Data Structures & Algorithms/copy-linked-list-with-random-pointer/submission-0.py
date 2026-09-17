"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        i = head
        nodeMap = {None:None}
        while i:
            nodeMap[i] = Node(i.val)
            i = i.next
        i = head
        while i:
            nodeMap[i].next = nodeMap[i.next]
            nodeMap[i].random = nodeMap[i.random]
            i = i.next
        return nodeMap[head]