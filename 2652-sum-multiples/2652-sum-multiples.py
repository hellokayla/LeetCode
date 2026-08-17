class Solution:
    def sumOfMultiples(self, n: int) -> int:
        nums = list(range(1,n+1))
        res_sum = 0
        for num in nums:
            if (num%3 == 0 or num%5 == 0 or num%7 == 0):
                res_sum += num
        return res_sum
        