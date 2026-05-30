class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #index like 0, 1, 2, ... represents each interval List[i]
        #List[i][j] - can go into each specific number
        #new interval might be smaller than first interval
        #doing cases but this is definitely not the way to do it
        res = []
        #where final result will be stored
        for i in range(len(intervals)):
            #go through every interval
            if newInterval[1] < intervals[i][0]:
                #checking the end of newInterval since sorted, huge!!!
                #no overlap and smaller case, easiest case just add at beginning
                res.append(newInterval)
                return res + intervals[i:]
                #add the rest now
            elif newInterval[0] > intervals[i][1]:
                #exists but comes after, so have to check all the intervals in case of overlap
                res.append(intervals[i])
            else:
                #now we come to overlap case and how to fix
                newInterval = [min(newInterval[0], intervals[i][0]), 
                max(newInterval[1], intervals[i][1])]
                #take smaller start and larger end and then expand (ie why we use 0, 1 and min and max)
        res.append(newInterval)
        #now we can append after overlap fix case
        return res
        #ofc now we return lol
                           

                 
                

        