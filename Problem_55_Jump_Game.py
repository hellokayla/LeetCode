class Solution(object):
    def canJump(self, nums):
        max_reach = 0
        n = len(nums)
        for i,e in enumerate(nums):
            # index + steps it can take
            max_reach = max(max_reach, i + e)
            
            # for case 3,2,1,0,4
            # max_reach = 3 
            # index reaches end = 4
            if max_reach < i : return False
            
            if max_reach >= (n-1): return True
