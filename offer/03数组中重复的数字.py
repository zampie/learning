'''


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        memo = set()
        for i in range(len(nums)):
            if nums[i] in memo:
                return nums[i]
            else:
                memo.add(nums[i])




class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]





'''