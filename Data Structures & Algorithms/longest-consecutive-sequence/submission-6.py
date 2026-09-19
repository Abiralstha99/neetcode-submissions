class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0 
        for num in nums_set:
            # now num is the start of a sequence
            if num - 1 not in nums_set:
                length = 1
                while num + 1 in nums_set:
                    length += 1
                    num +=1
                max_seq = max(max_seq,length)
        return max_seq

            