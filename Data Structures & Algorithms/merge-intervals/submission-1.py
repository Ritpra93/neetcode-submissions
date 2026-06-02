class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #very similar to before, just trying to think how cases would work
        intervals.sort(key=lambda i : i[0])
        #sorts all intervals by their interval, makes sense cause can just compare start
        output = [intervals[0]]
        #output list being created
        for start, end in intervals[1:]:
            #skip first cause alr in output, then everything else
            lastEnd = output[-1][1]
            #end value to figure out merging
            if start <= lastEnd:
                #overlap cases
                output[-1][1] = max(lastEnd, end)

            else:
                output.append([start, end])
                #non overlap case just add
        return output
                

        