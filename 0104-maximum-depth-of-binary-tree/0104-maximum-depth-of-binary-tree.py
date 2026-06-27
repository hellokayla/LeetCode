# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.calcMaxDepth(root)

    def calcMaxDepth(self, node):
        if node is None:
            return 0

        left_depth = self.calcMaxDepth(node.left) +1
        right_depth = self.calcMaxDepth(node.right) +1
        return max(left_depth, right_depth)
        