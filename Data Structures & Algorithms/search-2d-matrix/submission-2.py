class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Doing 2 binary search : 1 across to find which array
        # 2nd to find inside the array 

        top = 0
        bottom = len(matrix) - 1

        while(top <= bottom):
            mid = (top + bottom) // 2

            # If target is less than first elem of the array
            if (target < matrix[mid][0]):
                bottom = mid - 1

            # If target is greater than last elem of the array
            elif (target > matrix[mid][-1]):
                top = mid + 1
            
            else:
                row = mid
                break
        
        if (top > bottom):
            return False
        # Now we know top and bottom are equal
        left = 0
        right = len(matrix[0]) - 1

        while(left <= right):
            mid = (left + right) // 2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True
        return False

