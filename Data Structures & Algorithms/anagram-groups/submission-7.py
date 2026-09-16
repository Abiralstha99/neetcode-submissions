'''
Brute force:
1. Sorting and adding to a dictionary
2. Return dict.values() length

1. Use a freq mapping 
2. Create array with [0] ; now for every letter +1 
3. The array will be same for matching anagram and use the tuple as a key cause list are mutable
4. Return dict.values() length
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for anagram in strs:
            freq = [0] * 26
            for char in anagram: 
                freq[ord(char) - ord('a')] += 1
        
            dict[tuple(freq)].append(anagram)
        return list(dict.values())