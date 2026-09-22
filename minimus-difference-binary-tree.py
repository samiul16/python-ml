# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        minDiff  = float("inf")

        def inorder(root):
            nonlocal prev,minDiff
            if(root is None): return

            inorder(root.left)

            if(prev is not None):
                diff = root.val - prev
                if(diff < minDiff): minDiff = diff 

            prev = root.val

            inorder(root.right)

        inorder(root)

        return minDiff    