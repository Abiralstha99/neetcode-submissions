'''
Go through the grid -> get the rotten fruit and count of fresh fruit
Add all the rotten fruits to the queue and start bfs from there -> multi-source bfs

For every layer add +1 to the totalMin, for every fresh fruit you found deduct it from the earlier fresh fruit count 

If foundFresh = 0 return totalMin else return - 1
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        numFresh = 0
        queue = deque()
        totalMin = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    numFresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        while numFresh > 0 and queue:
            layerSize = len(queue)
            for node in range(layerSize): 
                row,col = queue.popleft()
                newDir = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]
                for newRow, newCol in newDir:
                    if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == 1:
                        numFresh -= 1
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
            totalMin += 1
        return totalMin if numFresh == 0 else -1
