# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node=root
        count=0
        ans=None
        def helper(node):
            nonlocal count,ans
            if node is None:
                return
            if ans is not None:
                return
            helper(node.left)
            count+=1
            if count==k:
                ans=node.val
            if count < k:
                helper(node.right)
            return ans
        return helper(node)