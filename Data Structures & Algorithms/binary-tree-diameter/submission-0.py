# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def helper(root):
            nonlocal diameter

            if root is None:
                return 0
            left_depth=helper(root.left)
            right_depth=helper(root.right)
            diameter=max(diameter,left_depth+right_depth)

            return 1 + max(left_depth,right_depth)
        helper(root)
        return diameter