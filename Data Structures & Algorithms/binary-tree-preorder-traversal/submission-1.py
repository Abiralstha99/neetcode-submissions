# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preOrder = []
        stack = [root]
        if not root:
            return []
        while (len(stack) != 0 ):
            node = stack.pop()
            preOrder.append(node.val)
            # Add right and left child
            if (node.right):
                stack.append(node.right)
            if (node.left):
                stack.append(node.left)
        return preOrder