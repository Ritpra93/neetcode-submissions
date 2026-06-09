class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n-1
            #removes right bit, keep going until there is no right bit
            count += 1
        return count 
            
        
        