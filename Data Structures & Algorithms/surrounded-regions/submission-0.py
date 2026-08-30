class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #replace in regular board
        #edges would be first column, first row, last row, last column
        #The intuitive approach of finding regions completely surrounded by 'X' is error-prone.
        #need all 4 borders
        #need a temp marker
        #dfs is acting like a capture
        #don't need an actual visited array since putting in place
        rows, cols = len(board), len(board[0])
        #horizontally vertically
        directions = ([0, 1], [1, 0], [-1,0], [0,-1])
        def dfs(r, c):
            #order matters for bounds checking
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return 
            #this T acts like the visited array
            board[r][c] = "T"
            dfs(r +1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(rows):
                    #first row
                if board[r][0] == "O":
                        dfs(r, 0)
                    #last row
                if board[r][cols-1] == "O":
                        dfs(r, cols-1)

        for c in range(cols):
                    #first col
                if board[0][c] == "O":
                        dfs(0, c)
                    #last col
                if board[rows-1][c] == "O":
                        dfs(rows-1, c)
            #now go through the whole board, just replace in place remember
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    #replace temp back
                elif board[r][c] == "T":
                    board[r][c] = "O"



            
            
        

        