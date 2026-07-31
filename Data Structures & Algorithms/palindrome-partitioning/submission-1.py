class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #this is like similar to two pointers for palindrome, but with backtracking
        res = []
        subset = []
        def backtrack_func(p1, p2):
            if p2 >= len(s):
                #pointer 2 is the length of the string, so at the end
                    #if they're equal make copy and return you, know all subsets been built
                    res.append(subset.copy())
                    return 
            if self.palindrome(s, p1, p2):
                #helper makes it easier here to check if palindrome
                subset.append(s[p1 : p2 + 1])
                backtrack_func(p2+1, p2+1)
                subset.pop()
                #doing the same stack as before
            if p2 +1 < len(s):
                backtrack_func(p1, p2+1)
        backtrack_func(0,0)
        return res


    def palindrome(self, s, pointer1, pointer2):
            while pointer1 < pointer2:
                if s[pointer1] != s[pointer2]:
                    return False
                    #check if they're equal to make palindrome
                pointer1, pointer2 = pointer1 + 1, pointer2 -1
                #increment left side by one, right by minus one
            return True
            #know they are a palindrome

    

        