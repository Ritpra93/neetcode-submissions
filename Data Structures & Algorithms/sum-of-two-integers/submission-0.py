class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xffffffff 
        while b & mask:
            a, b = (a ^ b), (a & b) << 1
        return a & mask if b > 0 else a

        '''
        a = 0101  (5)
        b = 0011  (3)
        0101
0011
XOR
----
0110
a = a ^ b = 6

0101
0011
AND
----
0001

b = (a & b) << 1 = 2

a = 0110
b = 0010

xor is sum without carry since 1 ^ 1 = 0
and finds carry  1 and 1 = 1 when both are 1
<< 1 moves the bit, need this for doing sum
mask because integers are unbounded python

        '''
      
            
     

#enumerate gives index and value
 