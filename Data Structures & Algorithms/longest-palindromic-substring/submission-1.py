class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" #don't forgot you're returning string not length
        resLen = 0 #track length
        for i in range(len(s)):
            #odd length edge case
            l, r = i, i #start at middle since that allows for better complexity
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r -l + 1 ) > resLen:
                    res = s[l : r+1]
                    resLen = r-l +1
                l -= 1
                r += 1
            #even length case
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r -l +1
                l -=1
                r +=1
        return res




 
            

            
        