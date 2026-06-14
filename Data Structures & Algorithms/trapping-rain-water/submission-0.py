class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            #case where you have height not existing 
            return 0 
        l, r = 0, len(height)-1
        #left = beginning of array
        #right = end of array
        leftMax, rightMax = height[l], height[r]
        #we start maxes at where we currently are at
        res = 0
        while l < r:
            #we need left to be less than right so we don't repeat stuff
            if leftMax < rightMax:
                #know left max in the sense 
                l+=1
                leftMax = max(leftMax, height[l])
                # we know this is current biggest from left
                res += leftMax - height[l]
                #algorithm to calculate depth
            else:
                r -=1
                rightMax = max(rightMax, height[r])
                #keep track of largest from right
                res += rightMax - height[r]

                #algorithm to calculate depth
        return res
        