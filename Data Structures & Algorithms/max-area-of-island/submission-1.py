class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Go through every cell in the grid.
        If I find land that hasn't been visited:
        BFS that island

        For every new visited cell, add +1 to size of that island
        Keep a track of the largest island, and return it
        '''
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        visited = set()
        maxArea = 0 
        island = 0
        
        def bfs(r,c):
            area = 1
            queue = deque([(r,c)])
            visited.add((r, c))
            while queue:
                row,col = queue.popleft()
                newDir = [(row + 1,col),(row - 1, col), (row, col + 1),(row, col - 1)]
                for newRow, newCol in newDir:
                    if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                        queue.append([newRow, newCol])
                        area += 1
                        visited.add((newRow, newCol))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)
        return maxArea