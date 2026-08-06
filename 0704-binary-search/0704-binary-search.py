class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1 # keep the -1 here because of left <= right

        while (left <= right):
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target: # go up, remove left side + mid
                left = mid + 1
            else: # go down, remove right side + mid
                right = mid - 1
        return -1
        