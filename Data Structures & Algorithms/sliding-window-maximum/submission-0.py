class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      res = []

      for i in range(len(nums) - k + 1):
        #gives you window of length 3 and starts at index 0
        #5 -3 + 1 = 3
            res.append(max(nums[i:i+k]))

      return res
        