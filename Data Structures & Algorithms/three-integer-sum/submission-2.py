class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # SO, first let's take each number and look for - nums[i] = nums[j] + nums[k] 
        # every num will be nums[i]
        # 
        # 
        res = []
        nums.sort()
        for i in range(0,len(nums)):
            a = nums[i]
            left = i + 1
            right = len(nums) - 1
            if (i > 0 and  a == nums[i - 1]):
                continue
            while (left < right):
                sum = a + nums[left] + nums[right]
                # Now solve a two sum 
                if (sum > 0):
                    right -= 1
                elif (sum < 0):
                    left += 1
                else:
                    res.append([a,nums[left],nums[right]])
                    left += 1
                    while (nums[left] == nums[left - 1] and left < right):
                        left +=1
        return res

