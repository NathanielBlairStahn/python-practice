"""
1. - Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        needed = {(target-num): idx1 for (idx1,num) in enumerate(nums)}
        for idx2, num in enumerate(nums):
            if (num in needed) and (needed[num] != idx2):
                return (idx2, needed[num])

class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        needed = {}
        for idx, num in enumerate(nums):
            if num in needed:
                return (needed[num], idx)
            needed[target-num] = idx

def main():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution2()

    print(nums, target, solution.twoSum(nums, target), "Expected = (0,1)")

    nums = [2,7,11,15, 23, 5, 6,8,4]
    target = 29
    print(nums, target, solution.twoSum(nums, target), "Expected = (4,6)")

if __name__=="__main__":
    main()
