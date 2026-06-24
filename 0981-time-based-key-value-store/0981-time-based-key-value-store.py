import bisect
class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        self.values = defaultdict(list)

    # the key intuition is the "bar" value is at the same index as the timestamp.
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.times[key]
        # replaces:
        # left = 0
        # right = len(value)-1
        # res = ''
        # while left <= right: 
        #     mid = left + (right - left) // 2
        #     if value[mid][0] <= timestamp:
        #         left = mid + 1 
        #         res = value[mid][1]
        #     else:
        #         right = mid - 1
        idx_right  = bisect.bisect_right(timestamps, timestamp)
        # counts how many is <= timestamp
        # values: "foo" -> ["bar", "bar2"] timestamps: "foo"-> [1, 4]
        res = self.values[key][idx_right-1] if idx_right else ""
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

