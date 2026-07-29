# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        def height(root):
            nonlocal balance
            if root is None:
                return 0
            lheight = height(root.left) 
            rheight = height(root.right)

            if abs(lheight - rheight) > 1:
                balance = False
                return 0
            return 1 + max(lheight, rheight)
        height(root)
        return balance