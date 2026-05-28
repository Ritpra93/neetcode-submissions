class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) +1) ] for i in range(len(text1)+1)]
        #creates the 2x2 matrix
        '''
        if
        len(text1) = 3
        len(text2) = 2
            dp = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0]
            ]
        add +1 because we eventually go out of bounds, empty string is always zero
        '''
        for i in range(len(text1)-1, -1, -1):
            #going backwards so we can calculate bottom up
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    #characters match so add one, do[i+1][j+1] because we are going up
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                    #don't match case, so we either skip or match
                    #take the best option, ie the max between dp[i][j+1]
                    #Second option is dp[i+1][j]
                    #if match diagonal = take it, if not skip one from either string, left or right
        return dp[0][0]
        #back at the top now