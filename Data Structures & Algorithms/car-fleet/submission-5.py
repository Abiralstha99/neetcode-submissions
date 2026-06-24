class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = zip(position,speed)
        for p,s in sorted(cars)[::-1]:
            time = (target - p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)