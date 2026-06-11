class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)

        for i, num in enumerate(nums):
            x ^= i #expected number
            x ^= num #actual number from array
            #0, 1 , 2
            #3, 0, 2
            #neat little trick where only the ones not matched left

        return x

    #i = 2
#num = 1

#Calculation:

#x = 1 ^ 2 ^ 1

  #x = 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 5 ^ 1 ^ 4 ^ 2

   #x = (1 ^ 1) ^ (2 ^ 2) ^ (4 ^ 4) ^ (5 ^ 5) ^ 3
   #ends up being 3
        


        