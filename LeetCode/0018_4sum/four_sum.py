"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class BruteForceSolution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        found = set()
        for ai, a in enumerate(nums):
            for bi, b in enumerate(nums[ai+1:]):
                for ci, c in enumerate(nums[ai+bi+2:]):
                    for di, d in enumerate(nums[ai+bi+ci+3:]):
                        if a+b+c+d == target:
                            found.add(tuple(sorted([a,b,c,d])))
        return [list(quadruplet) for quadruplet in found]

class BetterSolution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        needed = {}
        found = set()
        for ai, a in enumerate(nums):
            for bi, b in enumerate(nums[ai+1:]):
                if a+b in needed:
                    needed.add(tuple(sorted([a,b])))
                    found.add(tuple(sorted(needed[a+b]+[a,b])))
                else:
                    needed[target-(a+b)] = set(tuple(sorted([a,b])))
        return list(found)

if __name__=="__main__":
    nums = [1, 0, -1, 0, -2, 2]
