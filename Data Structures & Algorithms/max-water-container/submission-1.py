class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max = 0 
        while(left < right):
            breadth = right - left
            height = min(heights[left],heights[right])
            area = height * breadth 
            if (area > max):
                max = area
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -=1
        return max