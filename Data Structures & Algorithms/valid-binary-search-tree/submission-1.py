# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower=float('-inf')
        upper=float('inf')
        def helper(root,lower,upper):
            if root is None:
                return True
            if not lower < root.val < upper:
                return False
            left=helper(root.left,lower,root.val)
            right=helper(root.right,root.val,upper)

            return left and right
        return helper(root,lower,upper)
