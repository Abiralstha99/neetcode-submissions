class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_map = defaultdict(list)
        for course,pre in prerequisites:
            preq_map[course].append(pre)
        
        visited = set()

        def dfs(course):
            if (len(preq_map[course]) == 0):
                return True
            if course in visited:
                return False
            visited.add(course)
            for preq in preq_map[course]:
                # If duplicate is found in the stack, safely return false
                if not dfs(preq):
                    return False
            # Else remove from set, cause 2 course can have same prerequisite 
            visited.remove(course)
            preq_map[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

            
