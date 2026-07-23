class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while (l <= r):
            mid = (l + r) // 2
            # Check which side is sorted
            # True => left side is sorted
            if (nums[mid] == target):
                return mid
            if (nums[l] <= nums[mid]):
                if (nums[l] <= target and target < nums[mid]):
                    r = mid - 1
                else:
                    l = mid + 1
            # True => Right side is sorted
            else:
                if (nums[r] >= target and target > nums[mid]):
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
