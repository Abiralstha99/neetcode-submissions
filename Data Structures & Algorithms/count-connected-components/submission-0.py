class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        # Make a adj list 
        for node1,node2 in edges: 
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        visited = set()
        num = 0

        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)

            for neighbor in adj_list[node]:
                dfs(neighbor)
        
        for i in range(n):
            if i in visited:
                continue
            else:
                dfs(i)
                num += 1
        return num

