# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # function that takes root and returns depth of tree
        # rooted at "root"
        def depth(root):
            # base condition
            if root is None:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            max_depth = max(left_depth, right_depth) + 1
            return max_depth
        
        depth = depth(root)
        return depth
        