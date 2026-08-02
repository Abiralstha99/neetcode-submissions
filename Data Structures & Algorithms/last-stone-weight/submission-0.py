class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Understand: list of stone, stone[i] = ith stone weight
        # Output: result after simulation
        # Take the two largest stone, do the operation, add the result back to the 


        # Plan : Since heap doesn't have a maxHeap, we convert every element negative
        # and use a min heap
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        # Now pop the top and convert back to positive
        while(len(stones) > 1):
            y = - heapq.heappop(stones)
            x = - heapq.heappop(stones)
            if (x < y):
                diff = y - x
                heapq.heappush(stones, - diff)
        if stones:
            return -stones[0]
        return 0
