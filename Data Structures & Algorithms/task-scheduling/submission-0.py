import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ''' Understanding: 
        input : List of tasks ; int n 
        The same task must be separately by n cycle
        '''

        count = Counter(tasks)
        maxHeap = [-nums for nums in count.values()]
        heapq.heapify(maxHeap)
        queue = deque() # [task_remaining, time_when_available]
        time = 0 

        while queue or maxHeap:
            time += 1
            if maxHeap:
                task = 1 + heapq.heappop(maxHeap)
                if task:
                    queue.append([task, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap,queue.popleft()[0])
        return time
        

        