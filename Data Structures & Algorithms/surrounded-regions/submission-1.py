'''
Plan:

Let's reverse the problem :

1. Instead of going from inside O to check if it's in the border or not
2. Let's go through the edges, add it to a queue and do a multisource bfs
4. Now for disconnected O inside, convert them to X 
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Let's go through the edges and add O to the queue
        queue = deque()
        visited = set()

        rows = len(board)
        cols = len(board[0])

        # Left 
        for i in range(0,rows):
            if board[i][0] == "O":
                queue.append((i,0))
                visited.add((i,0))
        
        # Bottom 
        for i in range(1,cols):
            if board[rows - 1][i] == "O":
                queue.append((rows-1,i))
                visited.add((rows-1,i))
        
        # Right
        for i in range(0,rows - 1):
            if board[i][cols-1] == "O":
                queue.append((i,cols-1))
                visited.add((i,cols-1))

        # Top
        for i in range(1,cols - 1):
            if board[0][i] == "O":
                queue.append((0,i))
                visited.add((0,i))

        
        # Now start a multi-source bfs
        while queue: 
            row,col = queue.popleft()
            newDir = [(row + 1,col), (row - 1,col), (row, col+1), (row, col-1)]
            for newRow,newCol in newDir:
                if 0 <= newRow < rows and 0 <= newCol < cols and board[newRow][newCol] == 'O' and (newRow,newCol) not in visited:
                    queue.append((newRow, newCol))
                    visited.add((newRow,newCol))
            
        
        # After that loop through the matrix and O not in set, set to X
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    board[r][c] = "X"


