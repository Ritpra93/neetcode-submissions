class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0] #something to store said max
        currentSum = 0 #figure out current sum
        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n # add to current sum if > 0
            maxSum = max(maxSum, currentSum) #keep checking to see what max is
        return maxSum #return after u found it
        