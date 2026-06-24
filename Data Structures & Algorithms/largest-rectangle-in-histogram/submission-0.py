class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Increasing monotonic stack
        stack = []
        maxArea = 0 
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                # POP and then calculate the area
               index, height = stack.pop()
               maxArea = max(maxArea, height * (i - index))
               start = index
            stack.append((start,h))

        # There might still be some elements left in the stack
        for i,height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))
        return maxArea