class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create an empty dictionary to store num
        numMap = {}
        # get the length of the input list
        n = len(nums)

        # for loop to iterate over each index and create a compliment variable for the difference between the target number and current number
        for i in range(n):
            complement = target - nums[i]
            # if compliment is in numsMap, current number and compliment number is equal the target
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([3,3], 6))

#The time complexity of the provided Python code is O(n), where n is the length of the input list nums.
# This is because the algorithm only makes a single pass through the list nums
