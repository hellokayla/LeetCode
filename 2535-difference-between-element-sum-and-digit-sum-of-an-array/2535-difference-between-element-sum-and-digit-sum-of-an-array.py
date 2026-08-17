class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum, digit_sum = 0, 0
        for num in nums:
            element_sum += num
            if num >= 10:
                digits = [int(x) for x in str(num)]
                digit_sum += sum(digits)
            else:
                digit_sum += num
        
        return abs(element_sum-digit_sum)
        