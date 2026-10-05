class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        # Create a adj list
        for node1,node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
        
        # visited set to keep track 
        visited = set()

        # number of connected components
        num = 0

        # Helper function 
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for neighbor in adj_list[node]:
                dfs(neighbor)
            
        # DFS for every key in the adj_list
        for node in range(n):
            if node not in visited:
                num += 1
                dfs(node)
        return num
        
