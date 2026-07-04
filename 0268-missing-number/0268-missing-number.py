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

    Approach #3:
    Create a set, removing duplicates from the nums
    Loop through to find the missing number

    Approach #4: Bitwise XOR
    XOR both lists
    '''
    def missingNumber(self, nums: List[int]) -> int:
        '''
        missing = len(nums) = 3

        i=0, num=3:
        missing ^= 0  → missing = 3 ^ 0 = 3
        missing ^= 3  → missing = 3 ^ 3 = 0  ← 3 cancels with itself!

        i=1, num=0:
        missing ^= 1  → missing = 0 ^ 1 = 1
        missing ^= 0  → missing = 1 ^ 0 = 1

        i=2, num=1:
        missing ^= 2  → missing = 1 ^ 2 = 3
        missing ^= 1  → missing = 3 ^ 1 = 2

        return 2 ✓


        result = 3 XOR 0 XOR 1 XOR 0 XOR 1 XOR 2 XOR 3

        Group matching pairs:
        result = (0 XOR 0) XOR (1 XOR 1) XOR (3 XOR 3) XOR 2

        Apply a XOR a = 0:
        result = 0 XOR 0 XOR 0 XOR 2

        result = 2 ✓
        '''
        missing = len(nums)

        for i, num in enumerate(nums):
            missing ^= i
            missing ^= num
        return missing

        