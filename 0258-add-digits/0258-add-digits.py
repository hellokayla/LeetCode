class Solution:
    def addDigits(self, num: int) -> int:
        
      curr_sum_len = len(str(abs(num)))

      if curr_sum_len == 1:
        return num
    
      curr_sum = 0
      while curr_sum_len != 1:
        # calculate new curr sum
        curr_sum_len = len(str(abs(num)))
        nums = list(str(abs(num))) # ['3', '8]
        curr_sum = 0
        for n in nums:
            curr_sum += int(n)
        num = curr_sum
            

      return curr_sum