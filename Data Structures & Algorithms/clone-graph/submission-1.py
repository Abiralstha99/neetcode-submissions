"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
Plan: 
1. DFS across the graph, use a visited hashmap instead of set to track the cloned node.
2. First time you see a node -> create clone, create dict[node] = node-clone, add node to queue
3. You find a duplicate node -> ignore it
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        dict = {}

        def dfs(node):
            if node in dict:
                return dict[node]
            
            copy = Node(node.val)
            dict[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)