from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        d = defaultdict(int)

        # get the frequency mapping
        # 1 -> 3, 2-> 2, 3-> 1
        for n in nums:
            d[n] += 1

        # by defeault it's min heap
        
        for elem, freq in d.items():
            heap_value = (-1*freq, elem)
            heapq.heappush(max_heap, heap_value)
        
        res = []
        for _ in range(0, k):
            element = heapq.heappop(max_heap)[1]
            res.append(element)
        
        return res
        
        
            

        