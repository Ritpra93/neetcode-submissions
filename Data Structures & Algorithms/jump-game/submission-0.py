class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1 
        #have to reach the end of nums
        for i in range(len(nums)-1, -1, -1):
            #work backwards
            if i + nums[i] >= goal:
                #[1,2,0,1,0]
                #working backwards and seeing if it's possible to reach goal
                #can this index in fact reach the goal, if so make it the goal
                goal = i
        return True if goal == 0 else False
        #goal == 0 means we've reached all the way to beginning and can reach goal, ekse nah