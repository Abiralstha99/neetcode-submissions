'''
Understand: 
 -1 : water
 0 - treasure
 INF - Land 

Plan: 

Use a multi-source bfs - cause we're measuring distance and there's multiple starting points
1. Add all the treasure to the initial queue
2. Pop and for every neighbor append to queue and replace curr +1 to it's value
3. Continue the same for remaining elements in the queue
'''

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            row,col = queue.popleft()
            dir = [(row + 1, col), (row - 1,col), (row, col + 1), (row, col - 1)]
            for newRow, newCol in dir:
                if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == INF:
                    grid[newRow][newCol] = grid[row][col] + 1
                    queue.append((newRow, newCol))