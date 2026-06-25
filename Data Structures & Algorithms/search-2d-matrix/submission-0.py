class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        #rows
        cols = len(matrix[0])
        #columns
        left = 0
        right = rows * cols -1 
        #gets amt of elements by doing rows * cols - 1
        #same idea as before for binary search

        while left <= right:
            mid = (left + right) // 2
            #same as before with binary search
            row = mid // cols
            col = mid % cols
            #this flattens the 2d matrix
            #mid = 5
            #cols = 4
            #indicies 0-3 first arr, so flattening tells you where you are
            #ie matrix[1][2] == 16, row 1 (second arr) value 2, makes it easier
            value = matrix[row][col]
            if value == target:
                return True
            elif value <= target:
                left = mid +1
            else:
                right = mid - 1
        return False
