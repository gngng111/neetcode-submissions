class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            p = left + (right - left) // 2
            if target == nums[p]:
                return p
            if nums[p] < target:
                left = p + 1
            else:
                right = p - 1

        return -1