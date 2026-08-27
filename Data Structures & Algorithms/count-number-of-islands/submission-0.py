'''
Plan: 
for every cell (r,c):
if grid[r][c] == 1 and not visited:
    island += 1
    bfs (r,c)
''' 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0

        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))
            while q:
                row,col = q.popleft()
                newDir = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
                for newRow, newCol in newDir: 
                    if 0 <= newRow < rows and 0<= newCol < cols and grid[newRow][newCol] == "1" and (newRow,newCol) not in visited:
                        q.append((newRow,newCol))
                        visited.add((newRow, newCol))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island += 1
        return island

       

      
    
