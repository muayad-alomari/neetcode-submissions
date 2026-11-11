"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        i = 1
        n = len(intervals)
        intervals.sort(key =lambda i : i.start)
        while i < n:
            l1,l2=intervals[i-1],intervals[i]
            if l1.end > l2.start:
               return False
            i +=1 
        return True               

