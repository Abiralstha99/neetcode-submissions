class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # let's create a dictionary
        dict = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        # Now loop through the input
        for item in s:
            if item in dict:
                if stack and stack[-1] == dict[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return len(stack) == 0 
