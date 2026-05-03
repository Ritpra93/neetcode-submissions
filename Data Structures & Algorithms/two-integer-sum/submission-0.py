class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        '''
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[n], i] 
            hashMap[n] = i
        '''


        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[nums[i]] = i
        