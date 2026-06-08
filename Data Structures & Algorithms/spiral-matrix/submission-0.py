class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #increment to the right until you hit the end
        #go down until you can't 
        #go to the left until you can't
        #go up until you can't
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        #these the define the current rectangle
        #left, right = 0, 3 
        #top, bottom = 0, 3 3x3 matrix
        while left < right and top < bottom:
            #continue until all rectangles visited 
            for i in range(left, right):
                #traverse top row
                res.append(matrix[top][i])
            top +=1
            for i in range(top, bottom):
                #traverse, top to bottom
                res.append(matrix[i][right-1])
            right -= 1
            if not (left < right and top < bottom):
                #to make sure rows are not processed over again
                break
            for i in range(right -1, left-1, -1):
                #now traverse backwards to get everything not traversed, minus one to shrink boundary
                res.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom-1, top -1, -1):
                #finish left side, minus one to shrink boundary
                res.append(matrix[i][left])
            left +=1
        return res
        