# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, max_so_far):
            nonlocal res
            if not node:
                return
            if node.val >= max_so_far:
                res += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, max_so_far)
                dfs(node.right, max_so_far)
        dfs(root, float("-inf"))
        return res