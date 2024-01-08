class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # create an empty set
        hashSet = set()

        # iterate over each element in nums list
        for n in nums:
            # if current element in hashSet, return true
            if n in hashSet:
                return True
            # if current element not in hashSet, add it to the set
            hashSet.add(n)
        # otherwise
        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

# The time complexity of this code is O(n), where n is the length of the input list nums
