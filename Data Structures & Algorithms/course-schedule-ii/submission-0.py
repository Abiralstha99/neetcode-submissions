'''
Plan: 
1. Similar to course schedule I : make a adjacency list 
2. Start traversing using dfs. Look if there is a cycle or not 
3. If yes -> return []
4. If no -> when returning, you remove from the visited set, cause 2 course can have same prerequisite . Create a new result list and add the removed node to the list
5. Return the list


We have 3 state 

1. visited -> course has been added to result
2. visiting -> course added to path but not result
3. not visited -> neither result or path
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq_map = defaultdict(list)
        res = []
        visited = set()
        path = set()

        # Create a adjacency matrix
        for course, preq in prerequisites:
            preq_map[course].append(preq)
        
        # Now start traversing 
        def dfs(course): 
            # Check if it requires any preq
            if course in visited:
                return True
            
            # Check for cycle
            if course in path:
                return False

            path.add(course)

            # Loop through every preq of the course
            for preq in preq_map[course]:
                if not dfs(preq):
                    return False

            # We're now traversing back 
            visited.add(course)
            path.remove(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res 





