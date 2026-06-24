class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while(l < r):
            breadth = r - l
            height = min(heights[l], heights[r])
            area = breadth * height
            res = max(res,area)
            if (heights[r] > heights[l]):
                l += 1
            else:
                r -= 1
        return res