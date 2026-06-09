class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        #get rows and cols, cols = number of numbers in one array
        rowZero = False
        #don't make first row zero yet

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    #if we find a 0 make the whole column zero
                    if r > 0:
                        matrix[r][0] = 0
                        #or column zero
                    else:
                        rowZero = True
                        #row 1 zero 
        #first pass collect markers
        for r in range(1, rows):
            for c in range(1, cols):
                #first row and column contain markers
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    #set everything else to zero


        if matrix[0][0] == 0:
            #first column must be zeroed
            for r in range(rows):
                matrix[r][0] = 0

        if rowZero:
            #handle first row being zero
            for c in range(cols):
                matrix[0][c] = 0
 
        
        