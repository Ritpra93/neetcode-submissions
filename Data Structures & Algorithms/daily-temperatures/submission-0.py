class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        #answer never appears return zero
        stack = []
        #keeps temp and index [30 0]
        for i, t in enumerate(temperatures):
            #enumerate gives you index and temp
            while stack and t > stack[-1][0]:
                #checks if current temperature is warmer
                #and keep going until its not
                stackT, stackInd = stack.pop()
                #figure out the day that was warmer
                res[stackInd] = (i - stackInd)
                #compute days
            stack.append([t,i])
            #might need a warmer day in the future
            #[[75,0],[74,1],[72,2]]
            #[73,74,75,71,69,72,76,73] pop until this
        return res
            
        