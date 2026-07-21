# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:    
        cnt = 0
        val = -1
        def dfs(node):
            nonlocal cnt, val
            if not node:
                return 
            dfs(node.left)
            cnt += 1
            if cnt == k:
                val = node.val
                return
            dfs(node.right)    
        dfs(root)
        return val