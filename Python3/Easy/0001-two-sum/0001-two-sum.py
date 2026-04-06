class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        i = 0
        j = i+1

        while i < len(nums): 
            k = target - nums[i]
            print(k)
            while j < len(nums): 
                if nums[j] == k: 
                    return [i,j]
                else: 
                    j += 1
            i += 1
            j = i+1
            
        
