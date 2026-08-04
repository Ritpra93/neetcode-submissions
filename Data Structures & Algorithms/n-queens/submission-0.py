class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #maintain columns
        #rows don't matter cause we're moving each new row
        #set is great here so we don't have repeats
        #there is a pattern
        #r-c is constant, always 0 on diagonal
        #math for pos diagonal and negative diagonal
        #r+c for pos
        #try for all in first row
        #skip same column set, skip negative diagonal or positive diagonal
        #choose where no overlap
        # no two queens can attack each other.
        columns = set()
        #diagonals
        positive = set() #r+c
        negative = set() #r-c
        result = []
        board = [["."] * n for i in range(n)]

        def backtrack_func(row):
            if row == n:
                #remember how result is outputted
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            for col in range(n):
                if col in columns or (row+col) in positive or (row-col) in negative:
                    continue 
                    #skip it
                columns.add(col)
                positive.add(row+col)
                negative.add(row-col)
                board[row][col] = 'Q'

                #increment
                backtrack_func(row+1)

                #undo everything in backtracking, remember output
                columns.remove(col)
                positive.remove(row+col)
                negative.remove(row-col)
                board[row][col] = "."
        backtrack_func(0)
        return result
        #base case is start at 0

