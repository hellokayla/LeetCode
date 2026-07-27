class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. sort everything by start_time in place
        intervals.sort(key=lambda x:x[0])
        merged = []

        start_curr, end_curr = intervals[0]

        for i in range(1, len(intervals)):
            start_next, end_next = intervals[i]

            # mark new end_curr
            if end_curr >= start_next:
                end_curr = max(end_curr, end_next) 
            else:
                merged.append([start_curr, end_curr])
                # move pointer
                start_curr, end_curr = start_next, end_next
        # merge in start_curr, end_curr from the else
        merged.append([start_curr, end_curr])
        return merged

        