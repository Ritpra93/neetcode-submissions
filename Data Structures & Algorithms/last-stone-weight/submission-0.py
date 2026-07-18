class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heaviest stones so use a max heap, because max stones each iteration
        #rest of the instructions are the same
        #logn operation, * n = nlogn operation
        #do this using a min heap using negatives, ie biggest would be -8
        stones = [-s for s in stones]
        #multiple all stones by negative one
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                #first = -8, second = -7
                #since its flipped cause we using min heap
                heapq.heappush(stones, first - second)
        stones.append(0)    
        #in the case stones is empty edgecase    
        return abs(stones[0])
        #in case we have negatives in the stones arr

        