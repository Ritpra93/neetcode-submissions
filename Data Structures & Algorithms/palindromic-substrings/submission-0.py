class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i : j+1]
                if sub == sub[::-1]:
                    count += 1
        return count
        