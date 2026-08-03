class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''Understanding: input is a array may or maynot contain duplicate
        output is the kth largest elem
        [1,2,2,3], k = 2 => res = 2
        Match = kth largest => using a min heap
        Plan :
        1. Create a minheap from nums 
        2. Add each elem one by one
        3. If len(minHeap) > k: pop 
        4. Return minHeap[0] '''

        minHeap = []
        for i in range(len(nums)): 
            heapq.heappush(minHeap, nums[i]) # O(logk)
            if len(minHeap) > k: 
                heapq.heappop(minHeap) # O(logk)
        return minHeap[0]

# Space = O(k)
# Time = O(nlogk)
