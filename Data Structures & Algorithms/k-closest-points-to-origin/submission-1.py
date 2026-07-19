class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            #don't need to square root
            minHeap.append([dist, x, y])
            #appending to the min heap list like (8, 2, 2) -> first value is the dist so we can use that now

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            #do k times, cause theres a certain amount of k remember
            dist, x, y = heapq.heappop(minHeap)
            #remove smallest by dist
            res.append([x, y])
            #add coords
            k -= 1
            #decrement since we want to do k times
        return res
        #return results of distance
        