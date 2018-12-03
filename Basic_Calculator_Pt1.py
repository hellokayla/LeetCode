## String -> Calculator 
## ('6+9-12') = 3 
## ('1+2-3+4-5+6-7') = -2 
## ('1-2-3-4') = -8
## ('1+2-3+4-5+6-7') = -2
## ('255')
import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_nums = re.findall('\d+', s)
        
        ## grab the operators
        list_operators = ['+']
        for e in s:
            if e == "+" or e == "-": 
                list_operators.append(e)
        
        mult = 1 
        for i, e in enumerate(list_operators):
            if e == '-': 
                mult = -1
            if e == '+': 
                mult = 1
            list_nums[i] = int(mult) * int(list_nums[i])
        
        return sum(list_nums)