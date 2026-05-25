class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #not greedy this is a bottom up approach problem
        dp = [amount +1] * (amount +1)
        #amount+1 like an infinity value could never exceed
        dp[0] = 0
        #base case
        for a in range(1, amount+1):
            #for building bottom up, starting at 1 which is next number after base case
            for c in coins:
                #trying every coin from bottom up
                if a - c >= 0:
                    #doing the math
                    dp[a] = min(dp[a], dp[a-c] + 1)
                    #need to take minimum across all numbers
        return dp[amount] if dp[amount] != amount +1 else -1
        #case where it is the amount or amount does not exist
  

        
        



        