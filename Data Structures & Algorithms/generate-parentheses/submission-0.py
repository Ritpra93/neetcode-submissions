class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        #not a subset this ends up being a stack in this case
        #there was a similar problem to this one before
        count = 0

        def dfs(openPara, closedPara):
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
            if closedPara < openPara:
                #have to add closed parantheses remember
                subset.append(")")
                dfs(openPara, closedPara+1)
                subset.pop()
        dfs(0,0)
        #no parantheses to start with == base case
        return res
                


            
        

        