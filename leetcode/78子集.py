'''

# 循环
for num in nums:
    subset += [i + [num] for i in subset]

# 无序DFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(curr=[], star=0):
            output.append(curr)
            for i in range(star, len(nums)):
                dfs(curr + [nums[i]], i + 1)

        output = []
        dfs()
        return output


# 按顺序
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(curr=[],star=0):
            if len(curr) == k:
                output.append(curr)
            for i in range(star,len(nums)):
                dfs(curr+[nums[i]],i+1)

        output = []
        for k in range(len(nums)+1):
            dfs()
        return output


# BFS
from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        queue = deque()
        queue.append(([],0))
        len_nums = len(nums)
        output = []
        while queue:
            curr = queue.popleft()
            output.append(curr[0])
            for i in range(curr[1],len_nums):
                queue.append((curr[0]+[nums[i]],i+1))

        return output

'''
nums = [1,2,3]
subset = [[]]

for num in nums:
    subset += [i + [num] for i in subset]

subset


se = [[s1,s2] for s1 in nums for s2 in nums]

[s1+[s2] for s1 in se for s2 in nums]


nums = [1,2,3]
n = len(nums)
output = []

for i in range(2**n,2**(n+1)):

    bitmask = bin(i)[3:]
    print(bitmask)
    output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
    print(output)

def pr():
    print(k)

k=3
pr()


# DFS的循环写法
# -----------------------
nums = [1,2,3]
stack = [([], 0)]

# for j in range(6):
#     for i in range(j,len(nums)):
#         stack.append(nums[i])
#         output.append(stack[:])
#     j=len(stack)
#     stack.pop()

len_nums = len(nums)
output = []
while stack:
    curr = stack.pop()
    output.append(curr[0])
    for i in range(len_nums-1,curr[1]-1,-1):
        stack.append((curr[0] + [nums[i]], i + 1))

print(output)


