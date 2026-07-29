class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        #like combinations problem, sort for the adjacent one
        def dfs(i):
        #recursive function like 
        #where copy of subset will be built
            if i >= len(nums):
            #equals size of input
                res.append(subset.copy())
                return
            #skip, add, and adjacent duplicate case?
            subset.append(nums[i])
            copy_i = i
            dfs(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                #same way duplicates were checked before in combinations
                i += 1
            dfs(i + 1)
        dfs(0)
        return res

        