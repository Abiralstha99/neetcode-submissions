class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first let's combine the array 
        car_status = [[p,s] for p,s in zip(position, speed)]

        # we're gonna use a decreasing stack 
        stack = []

        for p,s in sorted(car_status):
            time = (target - p)/s
            while stack and stack[-1] <= time: 
                stack.pop() 
            stack.append(time)
        return len(stack)