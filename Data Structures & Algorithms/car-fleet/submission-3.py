class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first let's combine the array 
        car_status = [[p,s] for p,s in zip(position, speed)]

        # we're gonna use a decreasing stack 
        stack = []

        for p,s in sorted(car_status)[::-1]:
            time = (target - p)/s
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)