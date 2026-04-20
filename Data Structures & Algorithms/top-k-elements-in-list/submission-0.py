class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1

        return [item[0] for item in sorted(d.items(), key=lambda item: item[1])[-k:]]