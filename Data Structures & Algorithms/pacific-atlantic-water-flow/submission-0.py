'''
Plan:
1. Instead of going grid by grid; go reverse from ocean to grid 
2. Create two visited sets:
        pacific
        atlantic
3. Initialize the Pacific BFS with every cell touching the Pacific:
        entire top row
        entire left column2
4. Run BFS from ocean 
5. Find pacific N atlantic 
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        p_que = deque()
        p_set = set()

        a_que = deque()
        a_set = set()

        # Add top row to pacific
        for i in range(0, cols):
            p_que.append((0,i))
            p_set.add((0,i))

        # Add left col to pacific
        for i in range (1,rows):
            p_que.append((i,0))
            p_set.add((i,0))

        # Add botton row to atlantic
        for i in range (0, cols):
            a_que.append((rows - 1, i))
            a_set.add((rows - 1, i))
        
        # Add right col to atlantic
        for i in range (0, rows-1):
            a_que.append((i,cols-1))
            a_set.add((i,cols-1))

        # function that returns list of cells where water can flow to the ocean
        def flows(que, visit):
            while que:
                row,col = que.popleft()
                newDir = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]
                for newRow, newCol in newDir:
                    # Conditions for water to flow
                    if 0 <= newRow < rows and 0 <= newCol < cols and (newRow,newCol) not in visit and heights[newRow][newCol] >= heights[row][col]:
                        que.append((newRow,newCol))
                        visit.add((newRow, newCol))
            return visit
        
        cell_p = flows(p_que,p_set)
        cell_a = flows(a_que,a_set)

        return list(cell_p.intersection(cell_a))

