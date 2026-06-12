class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #always 9x9 
        #pointers in each box ?
        #l1 = board[i][0]
        #i2 = board[i2][0]
        #i3 = board[i3][0]
        #while i < 3> 
        #run three times?
        #i was close but real solution below
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        #key = (r // 3, c //3)
        #default dict = Python automatically creates an empty set when a key is first accessed.
        #sets = no duplicates, need this remember the requirements
        for r in range(9):
            #loop through rows
            for c in range(9):
                #loop through cols
                #remember the . is 
                if board[r][c] == ".":
                    #dw abt empty
                    continue
                if (board[r][c] in rows[r] 
                   or board[r][c] in cols[c] 
                   or board[r][c] in squares[(r//3, c //3)]):
                   #duplicate exists, based on three hashsets
                        return False
                #add board piece after each loop
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


