class Solution:
    def reverseBits(self, n: int) -> int:
         res = 0
         for i in range(32):
            first_bit = n & 1 #gets the rightmost bit, keeps only when 1
            res = (res << 1) | first_bit
            ##res << 1 -> move everything to left, then place rightmost bit in 
            n = n >> 1
            #move n to get next number, by removing bit we just added
         return res
        #basically being built from the ground up
        