class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        s = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        if carry == 0:
            if s > 0x7FFFFFFF: # neg numbers
                return ~(s ^ mask) # flip the bits
            return s
        else:
            return self.getSum(s, carry)
