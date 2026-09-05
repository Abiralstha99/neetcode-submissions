'''
Input: integer array nums, integer k
Output: k elements that appear most frequently

Plan: 
1. Use counter to make a dictionary 
2. Heapify the dictionary 0(n) with (frequency,key) tuple
3. Pop k times 
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)
        minHeap = []
        res = []
        # Dict = {1 : 3, 2: 2, 3:1}
        for num in dict.keys():
            heapq.heappush(minHeap, (dict[num],num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        # Now pop k times
        while k > 0:
            value,num = heapq.heappop(minHeap)
            res.append(num)
            k -= 1
        return res
            