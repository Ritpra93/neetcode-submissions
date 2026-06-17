class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        #double ended queue that stored indicies, not values
        #need to figure out if element has moved outside of window
        l = r = 0 
        while r < len(nums):
            #move right pointer through array
            while q and nums[q[-1]] < nums[r]:
                #this checks to remove all smaller elements, ie less than right pointer
                q.pop()
            q.append(r)
            #now add current index after removing smaller
            if l > q[0]:
                q.popleft()
                #remove elements not in current window, ie the left side for next loop
            if(r+1) >= k:
                #check if window reached length of k
                output.append(nums[q[0]])
                #maintained in decreasing order
                l += 1
                #move over left
            r+=1
            #now increment right after finishing window
        return output

 

     