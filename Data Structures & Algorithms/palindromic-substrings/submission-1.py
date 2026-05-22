class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #odd case
                res += 1 #case where you found a palindrome
                l -=1
                r += 1 
                #expand from the center remember
            l = i 
            r = i + 1
            #start the even case
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1 
                l -=1
                r += 1
        return res
