class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
    Finds the K most frequent elements in an array.

    Args:
        nums: The input array of integers.
        k: The number of most frequent elements to return.

    Returns:
        A list of the K most frequent elements.
        """
        if k == len(nums):
            return nums

        count = Counter(nums)
        heap = []

        for number, frequency in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (frequency, number))
            else:
                if frequency > heap[0][0]:
                    heapq.heapreplace(heap, (frequency, number))

        return [number for frequency, number in heap]