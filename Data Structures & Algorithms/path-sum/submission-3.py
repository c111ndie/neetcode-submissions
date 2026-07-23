# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ttl = 0
        def path(root, targetSum):
            nonlocal ttl
            if not root:
                return False
            ttl += root.val
            if ttl == targetSum and not root.left and not root.right:
                return True
            if path(root.left, targetSum):
                return True
            if path(root.right, targetSum):
                return True
            ttl -= root.val
            return False
        return path(root, targetSum)