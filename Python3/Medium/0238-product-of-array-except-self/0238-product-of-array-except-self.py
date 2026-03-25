class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        ans = [None] * len(nums)
        for i in range(0, len(nums)):
            prev = left[i]
            curr = nums[i]*prev # 1
            left.append(curr)

        for i in range(len(nums)-1, 0, -1):
            prev = right[len(nums)-1-i]
            curr = nums[i]*prev
            right.append(curr)
        
        right = right[::-1]

        for i in range(0, len(nums)):
            ans[i] = left[i]*right[i]
        
        return ans

