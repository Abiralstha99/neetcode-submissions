# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        while(stack):
            curr = stack.pop()
            if (curr.val < p.val and curr.val < q.val):
                stack.append(curr.right)
            elif (curr.val > p.val and curr.val > q.val):
                stack.append(curr.left)
            else:
                return curr
            