"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
Plan: 
1. BFS across the graph, use a visited hashmap instead of set to track the cloned node.
2. First time you see a node -> create clone, create dict[node] = node-clone, add node to queue
3. You find a duplicate node -> add it to dict[curr].neighbors list
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return 
        
        dict = {}
        queue = deque()
        queue.append(node)
        copy = Node(node.val)
        dict[node] = copy
        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in dict:
                    copy = Node(nei.val)
                    dict[nei] = copy
                    queue.append(nei)
                dict[curr].neighbors.append(dict[nei])
        return dict[node]
            








