from itertools import accumulate
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    # [-2,0,3,-5,2,-1]
    def sumRange(self, left: int, right: int) -> int:
        curr_list = self.nums[left:right+1]
        return self.prefixSum(curr_list)[-1]
    
    def prefixSum(self, nums):
        return list(accumulate(nums))
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)