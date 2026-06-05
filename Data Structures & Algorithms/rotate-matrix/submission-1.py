class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) -1
        while l < r:
          for i in range(r-l):
            top, bottom = l, r

            #save the topleft, we need a temporary so we don't lose original value
            #gets overwritten during swap
            topLeft = matrix[top][l+i]
            #intially topLeft = [0][0]

            #bottom left into top left
            matrix[top][l+i] = matrix[bottom-i][l]
            #did the math to figure out where bottom is
            #setting last value to next value

            #bottom right into bottom left
            matrix[bottom-i][l] = matrix[bottom][r-i]

            #move top right into bottom right
            matrix[bottom][r-i] = matrix[top+i][r]

            #move top left into bottom right
            matrix[top+i][r] = topLeft

          l+=1
            #increment so we can do the same for the inner sides of the square
          r-=1
       

'''
5x5 matrix
1   2   3   4   5
6   7   8   9  10
11 12  13 14  15
16 17  18 19  20
21 22  23 24  25
'''

'''
outer ring
1  2  3  4  5
6           10
11          15
16          20
21 22 23 24 25
'''

'''
inner ring
7  8  9
12   14
17 18 19
'''

'''
l = left boundary
r = right boundary
'''

#i = 0, 1, 2, 3
#(top, l+i)
#(bottom-i, l)
#(bottom, r-i)
#(top+i, r)

'''
top = 0
bottom = 4
l = 0
r = 4
i = 0
'''
'''
(0,0)
(4,0)
(4,4)
(0,4)
'''

'''
i = 1 case to help visualize
(0,1) - can see each one moved to the right to continue swapping
(3,0)
(4,3)
(1,4)
'''

'''
(row, col)
    ↓
(col, n-1-row)
'''