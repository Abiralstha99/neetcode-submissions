class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0 
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            # now num is the start of a sequence
            longest = 1
            while num + 1 in nums_set:
                num += 1
                longest += 1
            max_seq = max(max_seq,longest)
        return max_seq

            