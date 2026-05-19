class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 #empty list case
        if len(nums) == 1:
            return nums[0] #case where there is only one element
            #has to be MAX 
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1]) #max between both
        for i in range(2, len(nums)):
            #actually iterating through list now
            curr = max(prev1, prev2 + nums[i]) #since we want to compare the sums
            prev2 = prev1
            prev1 = curr
            #moving the values so you can figure out next biggest sum
        return prev1


  