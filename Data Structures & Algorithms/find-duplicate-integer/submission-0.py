class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd's Tortoise and Hare (Cycle Detection)
        '''
        Numbers are from 1 to n
        Array size is n+1
        so more indicies than possible values ie we can use Floyds
        there is a cycle entrance so they will meet, here it's the duplicate number since indicies > numbers
        '''
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            #slow moves one
            fast = nums[nums[fast]]
            #fast moves two steps
            if slow == fast:
                #they will eventually meet so break
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
        
       

        
        