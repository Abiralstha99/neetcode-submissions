'''
For a graph to be a valid tree:
1. No cycle
2. All the components must be connected : Keep a count of visited notes and check if visited == n 
3. Since the graph is undirected, pass prev into DFS.
   - If neighbor == prev, skip it because that's the edge we came from.
   - If we reach any other already visited node, there is a cycle.

Time: O(V + E)
- Each node is visited once.
- Each undirected edge is examined twice.

Space: O(V + E)
- Adjacency list: O(V + E)
- visited + recursion stack: O(V)
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = defaultdict(list)
        # COnvert to adj list
        for node1,node2 in edges: 
            adj_map[node1].append(node2)
            adj_map[node2].append(node1)
        
        # 
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            for child in adj_map[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False
            return True
        return dfs(0,-1) and len(visited) == n
         





