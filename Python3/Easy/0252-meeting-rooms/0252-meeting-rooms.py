class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # def(f(x)): return x[0]
        intervals.sort(key = lambda x : x[0])
        
        for i in range(1, len(intervals)):
            end_time_curr = intervals[i-1][1] # end time of curr interval
            start_time_next = intervals[i][0] # start time of next interval

            # in the event of a tie, you can't attend both meetings
            if end_time_curr > start_time_next:
                return False
        return True
        