#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。


nums = [2, 7, 11, 15]
target = 9

2 in nums

# n2
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(1,len(nums)-i):
#                 if nums[i] + nums[i+j] == target:
#                     return i,i+j
#
# 字典n1
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # for i in range(len(nums)):
#         #     for j in range(1,len(nums)-i):
#         #         if nums[i] + nums[i+j] == target:
#         #             return i,i+j
#         dic = {}
#
#         for i in range(len(nums)):
#             n2 = target - nums[i]
#
#             if n2 in dic:
#                 return [dic[n2], i]
#
#             dic[nums[i]] = i


dic = {}

for i in range(len(nums)):
    dic[nums[i]] = i

for i in range(len(nums)):
    n2 = target - nums[i]
    if n2 in dic:
        print([i,dic[n2]])
