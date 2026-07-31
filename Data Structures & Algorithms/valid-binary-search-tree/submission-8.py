# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Understand:
        ''' 1. Left Node < Root < Right Node
        2. Children must be binary 
        edge case: Having only one node'''\

        # Match: DFS

        # Plan: 
        '''Use a helper function to pass min and max range for left and right
        sub tree '''
        if root is None:
            return True

        def helper(root, left, right):
            if not root:
                return True
            if left >= root.val or root.val >= right:
                return False
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)
        return helper(root,float("-inf"), float("inf"))




