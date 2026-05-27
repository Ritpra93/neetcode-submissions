class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        #creating the bottom row, because can only move right
        #only one path to finish
        for i in range(m-1):
            #building rows upward
            newRow = [1] * n
            #new row, last column same way as row since you can only move down
            for j in range(n-2, -1, -1):
                #moving backwards
                newRow[j] = newRow[j+1] + row[j]
                #current cell = right + down
            row = newRow
        return row[0]


#dp[i][j] = dp[i][j+1] + dp[i+1][j]