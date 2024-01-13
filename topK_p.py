from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # create a counter variable
        counter = Counter(nums)
        return [x[0] for x in counter.most_common(k)]


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(solution.topKFrequent([1], 1))
