class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #we want the second largest or 3rd largest element, lets say we have 5,5
        #we'd want 4 for third largest
        #python lets do min heap again
        return heapq.nlargest(k, nums)[-1]