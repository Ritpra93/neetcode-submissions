class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emptyset = set()
        for i in range(len(nums)):
            if nums[i] not in emptyset:
                emptyset.add(nums[i])
            elif nums[i] in emptyset:
                return True
        return False
        