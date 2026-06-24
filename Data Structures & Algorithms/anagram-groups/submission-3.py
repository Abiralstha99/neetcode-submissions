class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for str in strs: 
            # Compute it's sorted value
            sortedStr = ''.join(sorted(str))
            dict[sortedStr].append(str)
        
        # Now return the list of value
        return list(dict.values())