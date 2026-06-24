class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        # results stores the output of the warmer temperature number
        result = [0] * len(temperatures)

        # Let's loop through the array
        for i in range(len(temperatures)):

            # We're using a decreasing stack here
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # If it's greater than the top element stack, it violates the property so
                # pop it out from the stack 
                prev_day = stack.pop()
                current_day = i
                num_days = current_day - prev_day
                result[prev_day] = num_days
            stack.append(i)
        return result