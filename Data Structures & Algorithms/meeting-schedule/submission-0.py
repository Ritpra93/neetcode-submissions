"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda i: i.start)
        #sorts intervals by start
        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            #get previous meeting
            i2 = intervals[i]
            #next meeting
            if i1.end > i2.start:
                #ends of first interval < second interval
                #remember you can have them be equal
                return False
                #so return false
        return True
        #else can safely return true
'''
intervals = [
    Interval(0, 30),
    Interval(35, 40),
    Interval(45, 50)
]
'''