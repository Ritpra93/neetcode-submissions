class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
           numberNeeded = target - nums[i]
           if numberNeeded in hashMap:
            return [hashMap[numberNeeded], i]
           hashMap[nums[i]] = i
        
           
     


       
        