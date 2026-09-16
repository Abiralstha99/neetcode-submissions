class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for anagram in strs:
            freq = [0] * 26
            for char in anagram: 
                freq[ord(char) - ord('a')] += 1
        
            dict[tuple(freq)].append(anagram)
        return list(dict.values())