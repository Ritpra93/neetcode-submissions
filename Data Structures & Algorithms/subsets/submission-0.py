class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def backtrack(start, current):
            output.append(current[:])  # snapshot of current subset
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return output
        
        