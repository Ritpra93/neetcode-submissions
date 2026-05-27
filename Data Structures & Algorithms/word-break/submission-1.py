class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        #creates a list [False, False, False, False]
        dp[len(s)] = True
        #mot starting at one in this case since we are working backwards
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    #s[i : i + len(w)] = s[0:5] == "apple"
                    dp[i] = dp[i + len(w)]
                    #current word matches, then the answer at i depends on if the remaining substring works
                if dp[i]:
                    break
        return dp[0]

'''
dp index meaning
0        "apple"
1        "pple"
2        "ple"
3        "le"
4        "e"
5        ""
'''
   