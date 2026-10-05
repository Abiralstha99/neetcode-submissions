'''
WHat makes a valid tree ? 
- A graph but w/o the cycle
- No disconnected component 
- Edge case : 0 ---- 1 ; Here only checking cycle would be wrong; so need to keep track of both prev, curr node 
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Make a adj list 
        adj_list = defaultdict(list)
        for node1,node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
        
        # Visited set to keep track
        visited = set()

        def dfs(prev,curr):
            if curr in visited:
                return False
            visited.add(curr)
            for neighbor in adj_list[curr]:
                if neighbor == prev:
                    continue
                if not dfs(curr,neighbor):
                    return False
            return True
        
        return dfs(-1,0) and len(visited) == n
        
            

        

        