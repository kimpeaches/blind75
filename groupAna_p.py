from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # create a dictionary-like object
        temp = defaultdict(list)
        # iterate over the characters in each string
        for c in strs:
            # sort the characters in each string
            temp[str(sorted(c))].append(c)
        # return the values of the dictionary
        res = list(temp.values())
        return res


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
