class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = dict()

        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        for val in counter.values():
            if val > 1:
                return True
        return False