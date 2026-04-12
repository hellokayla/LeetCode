class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        if len(intervals) == 1: return 1
        # step 1 - sort the start and end times
        start_times = [interval[0] for interval in intervals]
        end_times = [interval[1] for interval in intervals]
        start_times = sorted(start_times)
        end_times = sorted(end_times)

        # step 2 - use two pointer method for checking room availability
        max_rooms, rooms = 0, 0
        i, j = 0, 0
        while (i < len(start_times) and j < len(end_times)):
            # am i starting earlier than the last room opening?
            if start_times[i] < end_times[j]:
                rooms += 1 # open up a room since nothing is freed up
                i += 1 # continue with next start time
            # is my start time later than the last end time?
            # is a room free?
            elif start_times[i] >= end_times[j]: # else also works
                i += 1
                j += 1 # we freed up a room, to the next end time
            max_rooms = max(max_rooms, rooms)
        return max_rooms        
''' 
    Brute Force O(I*I) solution
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # step 1 - get the start and end time
        min_start, max_end = float("inf"), float("-inf")
        for interval in intervals:
            curr_start = interval[0]
            curr_end = interval[1]

            min_start = min(curr_start, min_start)
            max_end = max(curr_end, max_end)
        
        # step 2 loop through curr time and get max rooms
        max_rooms = 0
        for curr_time in range(int(min_start), int(max_end)): # 0, 30 at 15
            rooms_reserved = 0 #0
            for interval in intervals: # [15, 20]
                start_time = interval[0] # 15
                end_time = interval[1] # 20
                if start_time <= curr_time < end_time: # 
                    rooms_reserved += 1 # 2

            max_rooms = max(max_rooms, rooms_reserved) #2
        return max_rooms
'''