"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #don't track individual rooms, track amount of simulateneous meetings
        start = sorted([i.start for i in intervals])
        #have an array that is sorted from the start
        end = sorted([i.end for i in intervals])
        #have an array that is sorted from the end
        #start = occupied, end = free
        res, count = 0,0
        #active meetings
        s, e = 0,0
        #track next start and end time
        while s < len(intervals):
            #go through all meeting starts
            if start[s] < end[e]:
                #whole trick to see active meetings
                #compare starting and ends, determines need another meeting room since
                #it one is already going on
                s+=1
                count+=1
            else:
                e+=1
                #move to the next ending meeting
                count-=1
                #decrement since meeting ended
            res = max(res,count)
            #based on what was tracked find the max of the most active meetings, since that will be the min
        return res
        