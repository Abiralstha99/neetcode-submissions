# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Understand : Display all the nodes that are visible from the right side

        # Match : BFS 

        # Plan:  
        # 1. Go each level -> From left to right, 
        # 2. find the last elem of that level and add it -> res []

        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while (queue):
            lenQ = len(queue)
            for i in range(lenQ):
                node = queue.popleft()
                if i == lenQ - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
