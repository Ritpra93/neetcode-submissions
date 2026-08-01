class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash = {"" : [], "2" : "abc", "3" : "def", "4" : "ghi", "5" :       "jkl",  "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        res = []
        subset = []
        def backtrack_function(i, string):
            #split string until empty then return?
            #why is it only two pairs and not multiple 
            #ohh only choosing on character per numbers 
            #strings immutable so don't have to pop
            if len(string) == len(digits):
                #we picked a letter for every digit
                res.append(string)
                return
            for s in hash[digits[i]]:
                    #hash[2] = abc, since digits[i] -> gets number
                    #for character in abc
                    backtrack_function(i+1, string + s)
                    #goes throught the hash, incrementing i based on s
                    #backtrack_function(increase i to next digit, "choose a letter ie a or b or c, do that for each letter")
        if digits:
            backtrack_function(0, "")
            #base case, i starts at 0, empty string to begin with
        return res


        