class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        k = nums[left]
        while (left <= right):
            mid = (left + right) // 2
            # Now see which half is sorted

            # True => Left half is sorted
            if (nums[left] <= nums[mid]):
                k = min(k,nums[left])
                left = mid + 1 # now check if the min lies in RHS
            
            # True => right half is sorted
            elif (nums[right] > nums[mid]):
                k = min(k,nums[mid])
                right = mid - 1
        return k