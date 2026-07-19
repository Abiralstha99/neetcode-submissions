
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        hr = 0 
        k = 0 
        while(left <= right):
            mid = (left + right) // 2

            # Now check how much hour will it take
            for num in piles:
                hr = hr + math.ceil(num/mid)
            
            if (hr <= h):
                right = mid - 1
                k = mid
            elif (hr > h):
                left = mid + 1
            hr = 0
        return k
