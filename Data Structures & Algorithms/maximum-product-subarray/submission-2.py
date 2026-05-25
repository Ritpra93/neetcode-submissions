class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #it is bottom up but i'm doing it wrong
        currentMax = nums[0]
        result = nums[0]
        currentMin = nums[0]
        #case where you only have one nums
        for i in range(1, len(nums)):
            track_num = nums[i]
            temporaryMax = max(track_num, track_num * currentMax, track_num * currentMin)
            currentMin = min(track_num, track_num * currentMax, track_num * currentMin)
            currentMax = temporaryMax
            result = max(result, currentMax)
        return result



        