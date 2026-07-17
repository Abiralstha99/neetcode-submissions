# Using array instead of hashmap
class Solution: 
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        n1, n2 = len(s1), len(s2) 
        if len(s1) > len(s2): 
            return False 
        s1Count, s2Count = [0] * 26, [0] * 26 

        for i in range(n1): 
            s1Count[ord(s1[i]) - ord('a')] += 1 
            s2Count[ord(s2[i]) - ord('a')] += 1 
        left = 0
        for i in range(n1, n2): 
            if s1Count == s2Count: 
                return True 
            # remove leftmost character
            s2Count[ord(s2[left]) - ord('a')] -= 1 
            left += 1
            s2Count[ord(s2[i]) - ord('a')] += 1 
        return s1Count == s2Count