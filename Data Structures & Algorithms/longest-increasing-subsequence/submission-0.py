class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #my guess bottom up approach like before
        dp = [1] * len(nums)
        #set up dp array like before
        for i in range(len(nums)):
            for j in range(i):
                #we want indexes so loop through j
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] +1)
                    #increasing subsequences, then get the max
        return max(dp)
        #need max over all the positions
