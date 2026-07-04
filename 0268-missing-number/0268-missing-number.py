class Solution:
    # Input: nums
    # Output: return nums that are missing
    
    ''' 
    Brute force:
    Approach #1:
    Sort the nums O(n log n), then loop through, returning the missing numbers.

    Approach #2:
    Allocate a map = [0] * len(nums)+1
    Go through every value in nums, mapping it to the 1D map.
    '''
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        nums_map = [0] * (len(nums)+1)
        # [3,0,1]
        # [0,0,0,0]
        for n in nums:
            nums_map[n] += 1

        for i in range(0, len(nums_map)):
            if nums_map[i] == 0:
                return i
        return 0
        
        