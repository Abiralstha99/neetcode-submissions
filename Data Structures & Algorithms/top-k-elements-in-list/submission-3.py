'''
Plan
Using bucket sort 
1. Build frequency map 
2. freq[i] will store number that comes i times
3. Add the key,value pair to a freq[frequency] list
4. Now, loop from behind and add it to res list until k times
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res =[]
        dict = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        # Append values to freq list
        for num, value in dict.items():
            freq[value].append(num)
        
        for i in range (len(freq) - 1, 0 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        



        