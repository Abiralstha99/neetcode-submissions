from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0 
        right = len(s1)
        dict_s1 = dict(Counter(s1))
        dict_s2 = dict(Counter(s2[left:right]))
        for right in range(len(s1), len(s2)):
            if (dict_s1 == dict_s2):
                return True
            else:
                dict_s2[s2[right]] = dict_s2.get(s2[right],0) + 1
                dict_s2[s2[left]] -= 1

                # We are only removing value by 1, so if any key's value is 0, we remove them
                # from dict
                if dict_s2[s2[left]] == 0:
                    del dict_s2[s2[left]]
                left += 1
        # The room doesn't check for the last elem, so in the end we return by checking the 2 dictionaries
        return dict_s1 == dict_s2