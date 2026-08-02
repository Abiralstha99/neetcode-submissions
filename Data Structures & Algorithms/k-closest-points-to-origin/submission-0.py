class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ''' Understand: We're given array of coordinates, output = k closest point to origin
        k closest = maxHeap
        Plan: Make a tuple, ([x,y], dist) then make a maxHeap using dist and add the end return a 2d list with (x,y) only'''

        maxHeap = []
        res = []
        for x,y in points:
            dist = (x**2) + (y**2)
            # Now add this to heap
            heapq.heappush(maxHeap, (-dist,[x,y]))
            if (len(maxHeap) > k):
                heapq.heappop(maxHeap)
        # Now convert the tuple to list and return 
        for dist,points in maxHeap:
            res.append(points)
        return res