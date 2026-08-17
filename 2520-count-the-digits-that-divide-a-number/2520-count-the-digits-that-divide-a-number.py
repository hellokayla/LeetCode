class Solution:
    def countDigits(self, num: int) -> int:
        digits = list(str(num))
        count = 0

        for digit in digits:
            if(num % int(digit) == 0):
                count += 1
        return count
