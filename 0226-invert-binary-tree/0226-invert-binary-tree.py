# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        q = Queue()

        if not root:
            return None

        q.put(root)
        res.append(root) # 4

        while not q.empty():
            for _ in range(q.qsize()):
                curr = q.get()
                # swap before enqueuing children
                # must swap in one go
                curr.left, curr.right = curr.right, curr.left
                if curr.left:
                    q.put(curr.left)
                    res.append(curr.left)
                if curr.right:

                    q.put(curr.right)
                    res.append(curr.right)
                

        return res[0]


        