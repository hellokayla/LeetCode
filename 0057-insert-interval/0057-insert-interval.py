class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # no need to sort by start
        merged = []

        for i in range(0, len(intervals)):
            start_curr, end_curr = intervals[i]
            start_new, end_new = newInterval

            # [1,2] newInterval ->[[3,4],[5,6]] Intervals
            if end_new < start_curr:
                merged.append(newInterval)
                merged.extend(intervals[i:])
                return merged
            # [5,8] newInterval ->[[1,3]] Intervals
            # append current Interval, keep going
            elif start_new > end_curr:
                merged.append([start_curr, end_curr])
            # [4,8] newInterval-> [[5,6]] Intervals
            # min(4,5) = 4 max(8,6) = 8 -> [4,8]
            # is overlapping, merge
            else:
                newInterval = [(min(start_new, start_curr)), (max(end_new, end_curr))]

        merged.append(newInterval)
        return merged
            