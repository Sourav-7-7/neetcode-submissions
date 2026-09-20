# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        node=root
        max_so_far=root.val
        def helper(node,max_so_far):
            if node is None:
                return 0
            
            cur_count= 1 if node.val >= max_so_far else 0
                
            if node.val >= max_so_far:
                max_so_far=node.val
            left=helper(node.left,max_so_far)
            right=helper(node.right,max_so_far)

            return cur_count+left+right
        return helper(node,max_so_far)
