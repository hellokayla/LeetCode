class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value)) # key: "foo" value: ("bar", 1)

    def get(self, key: str, timestamp: int) -> str:
        value = self.store.get(key, []) #should get out the value
        #print("value:", value)
        left = 0
        right = len(value)-1
        res = ''
        while left <= right: 
            mid = left + (right - left) // 2
            if value[mid][0] <= timestamp:
                #print("value[mid][0]:",value[mid][0])
                left = mid + 1 
                res = value[mid][1]
            else:
                right = mid - 1 
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

'''
p0 - we want to create a way to store this

'''