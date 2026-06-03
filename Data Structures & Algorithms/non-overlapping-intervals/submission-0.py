class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #greedy strategy is remove the interval that ends earlier
        intervals.sort()
        #want to process intervals from start to right to see where there is overlap to get non overlapping
        res = 0
        prevEnd = intervals[0][1]
        #just need to track end interval 
        #[[1,2], [2,4], [1,4]], would be 2
        for start, end in intervals[1:]:
            #skip first interval
            if start >= prevEnd:
                #case where there is no overlap 
                #ie 2 = 2, so becomes most recently kept 
                #start = 2
                #end = 4 for next interval
                #then you continue same way for next interval
                prevEnd = end
            else:
                #case where there is
                # 1 < 2, needs to be removed 
                res += 1
                prevEnd = min(end, prevEnd)
                #keep the one with the smaller end, gives room for more intervals
        return res
        

            
      

            
        