# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        def build(l, r):
            nonlocal pre_idx
            if l > r: 
                return None
            root = TreeNode(preorder[pre_idx])
            idx = indices[preorder[pre_idx]]
            pre_idx += 1
            root.left = build(l, idx - 1)
            root.right = build(idx + 1, r)
            return root
        return build(0, len(preorder) - 1)