class Solution:
    def numDecodings(self, s: str) -> int:
        #could use a hashmap that maps each alphabet character??
        #ohh but these cases weird since you can map multiple ways
        # 12 same as AB or L
        #1 number equals only one letter, 2 equals potentially 2 but depends if zero in the first place
        #would 3 be 3 letters?? could be upto 32 letters... ooh that makes this tough
        #but break down if letters > 2? since it becomes 2, 1 
       
        '''
        
        sum = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = sub[i, j+1]
                if sub[i] or sub[j+1] == 0:
                    i+=1
                    j+=1
                else:
                    #do I have to map back? realistically couldn't every combination of number equal another value?
                    sum += 1
                    #"226" has valid substrings "2", "22", "26", "2", "6" -> forgetting this

        '''
        #tons of wrong assumptions here
        #sequential decision problem, not a search/counting problem
        #"how many substrings" != "how many ways can I decode"
        #0 is not a simple skip condition
        #06 not valid, but 206 is, so you have to change based on that 
        #completely forgot these are strings not int
        length_s = len(s)
        dp = [0] * (length_s +1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        else:
            0 
        for i in range(2, length_s+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            two = s[i-2:i]
            if '10' <= two <= '26':
                dp[i] += dp[i-2]
        return dp[length_s]
