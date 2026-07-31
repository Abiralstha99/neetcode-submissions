# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Understand: Good node = There is no node X in it's path from root st X > node

        # Match = DFS

        # Plan = 
        # 1. Keeping a greater variable so that if node > greater, then it is a good node else
        # false.
        # 2. For every node, we will be setting a new greater
        # 3. If we pass a greater variable, then we can avoid recalculating every time for each
        # node. This makes it O(N)

        if root is None:
            return 0 
        res = 0
        max = root.val
        def helper(root, max):
            nonlocal res 
            if root is None:
                return 0
            if root.val >= max:
                max = root.val
                res+= 1
            helper(root.left, max)
            helper(root.right, max)
        helper(root, max) 
        return res