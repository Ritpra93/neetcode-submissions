class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        #not a subset this ends up being a stack in this case
        #there was a similar problem to this one before
        #add one, close one = stack behavior
        #thats why stack was used
        count = 0

        def dfs(openPara, closedPara):
            #there is no array, we are building it
            if openPara == closedPara == n:
                res.append("".join(subset))
                return
                #backtracking so last case as always
                #but remember what we are working with now
            #how do you get parantheses like that?
            if openPara < n:
                subset.append("(")
                dfs(openPara+1, closedPara)
                #track how much open parantheses vs closed parantheses
                subset.pop()
                #The last character added is always the first one removed, which is the definition of a stack.
                #each call cleans up after itself, so stack makes more sense here since we are backtracking
                #pop has to undo append
            if closedPara < openPara:
                #have to add closed parantheses remember
                subset.append(")")
                dfs(openPara, closedPara+1)
                subset.pop()
        dfs(0,0)
        #no parantheses to start with == base case
        return res
                


            
        

        