'''
Plan: 
1. Create a adj list 
2. Do a dfs ; before exploring neighbors add visit set to see if a node comes back to itself
3. If node in visited -> return false
4. If len(node) == 0 -> return True
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_map = defaultdict(list)
        # Create adj matrix
        for course, preq in prerequisites: 
            preq_map[course].append(preq)

        visited = set()

        def dfs(course):
            # Means this course is not a preq for any other course
            if not preq_map[course]:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)

            for preq in preq_map[course]:
                if not dfs(preq):
                    return False
                    
            visited.remove(course)
            preq_map[course] = []
            return True
        
        for i in range(numCourses): 
            if not dfs(i):
                return False
        return True

                