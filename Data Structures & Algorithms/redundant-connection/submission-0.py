'''
1. Use disjoint set 
2. For every edge in the list, start union-ing. 
3. If node1.parent == node2.parent ; it means there's a cycle. This is so because if they are equal then previously, we have already connected their neighbors and found a path 
4. Thus, the new edge is a 2nd path and will be a cycle
'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # Nodes are from 1 - N 
        parent = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def find(n):
            if n == parent[n]:
                return parent[n]
            parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]

        