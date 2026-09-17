'''
Understand:
1. Every row must contains unique
2. Every column must contain unique
3. Every 3*3 box must contain a unique

Plan:
1. Make a set for every row, col, and the box. 
2. If the number is unique to row,col and box, it's good 
3. Row and Col is normal n^2 check 
4. For the box: we can divide the row // 3 and col // 3 to get indication of where it belongs
5. Use a hashmap with tentative box position tuple as the key and set as a value
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check every row 
        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
                num = board[i][j]
                if num == ".":
                    continue
                if num in row:
                    return False
                row.add(num)

        # Check every column  
        for i in range(len(board)):
            col = set()
            for j in range(len(board[0])):
                num = board[j][i]
                if num == ".":
                    continue
                if num in col:
                    return False
                col.add(num)
        
        # Check every box
        box_map = defaultdict(set)
        for i in range(len(board)):
            box = set()
            for j in range(len(board[0])):
                box_row, box_col = i // 3 , j // 3
                if board[i][j] == ".":
                    continue
                if board[i][j] in box_map[(box_row,box_col)]:
                    return False
                box_map[(box_row,box_col)].add(board[i][j])
        return True

            