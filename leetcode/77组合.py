'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 循环
# -------------------
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        curr = [[i] for i in range(1, n + 1)]
        for _ in range(k-1):
            temp = []
            for i in range(len(curr)):
                temp += [curr[i]+[j] for j in range(curr[i][-1]+1,n+1)]
            curr = temp

        return curr

# 回溯
# ----------------
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def trackBack(start=1, curr=[]):
            if len(curr) == k:
                output.append(curr)
            for i in range(start, n + 1):
                trackBack(i + 1, curr + [i])

        output = []
        trackBack()
        return output



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        curr = [[i] for i in range(1, n + 1)]
        for _ in range(k-1):
            curr = [i+[j] for i in curr for j in range(i[-1]+1,n+1)]

        return curr


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = [i for i in range(1, n + 1)]
        curr = [[i] for i in nums]

        for _ in range(k-1):
            curr = [j+[i] for j in curr for i in nums[j[-1]:]]

        return curr

# My DFS
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(curr,other):
            if len(curr)==k:
                output.append(curr)
                return

            for i in range(len(other)):
                dfs(curr + [other[i]], other[i+1:])

        nums = list(range(1,n+1))
        output=[]
        dfs([],nums)

        return output
# DFS优化
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(curr=[],start=0):
            if len(curr)==k:
                output.append(curr)
                return

            for i in range(start,len_nums):
                dfs(curr + [nums[i]], i+1)

        nums = list(range(1,n+1))
        output=[]
        len_nums = len(nums)
        dfs()

        return output

# BFS 超时
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        output=[]
        queue = [([], nums)]

        while queue:
            curr = queue.pop(0)
            if len(curr[0]) == k:
                output.append(curr[0])
            if len(curr[0]) > k:
                break

            for i in range(len(curr[1])):
                queue.append((curr[0]+[curr[1][i]],curr[1][i+1:]))

        return output

# BFS 优化 依然 超时
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        start = 0
        output = []
        queue = [([], start)]
        len_nums = len(nums)

        while queue:
            curr = queue.pop(0)
            if len(curr[0]) == k:
                output.append(curr[0])
            if len(curr[0]) > k:
                break

            for i in range(curr[1], len_nums):
                queue.append((curr[0] + [nums[i]], i+1))

        return output


# BFS 用deque优化
1092ms,5.27%
from collections import deque
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        start = 0
        output = []
        queue = deque()
        queue.append(([], start))
        len_nums = len(nums)

        while queue:
            curr = queue.popleft()
            if len(curr[0]) == k:
                output.append(curr[0])
            if len(curr[0]) > k:
                break

            for i in range(curr[1], len_nums):
                queue.append((curr[0] + [nums[i]], i+1))

        return output
'''






n = 4

lis = [i for i in range(1, n + 1)]
res = []
for i in range(n - 1):
    res += [[lis[i], s] for s in lis[i + 1:]]

# ------------------------------

n = 5
k = 3


def backtrack(first=1, curr=[]):
    # if the combination is done
    if len(curr) == k:
        output.append(curr.copy())
    for i in range(first, n + 1):
        # add i into the current combination
        curr.append(i)
        # use next integers to complete the combination
        backtrack(i + 1, curr)
        # backtrack
        curr.pop()


output = []
backtrack()

# ----------------------------

n = 5
k = 3

output = []

curr = [[i] for i in range(1, n + 1)]

temp = []

s2 = 2
for i in range(len(curr)):
    curr[i] = curr[i] + [curr[i][-1]+1]


curr = [[i] for i in range(1, n + 1)]
for _ in range(k-1):
    temp = []
    for i in range(len(curr)):
        temp += [curr[i]+[j] for j in range(curr[i][-1]+1,n+1)]
    curr = temp
curr

curr = [i+[j] for i in curr for j in range(i[-1]+1,n+1)]






import itertools
list(itertools.combinations(range(1,n+1),k))


n = 20
k = 16

def trackBack(start=1, curr=[]):
    print(curr)
    if len(curr) == k:
        output.append(curr)
    for i in range(start, n + 1):
        trackBack(i + 1, curr + [i])


output = []
trackBack()

list(itertools.permutations([1,2,3]))














# --------------------
n=4
k=2
nums = [i for i in range(1, n + 1)]
curr = [[i] for i in nums]

curr = [j+[i] for j in curr for i in nums[j[-1]:]]


for _ in range(k-1):
    temp = []
    for i in range(len(curr)):
        temp += [curr[i]+[j] for j in range(curr[i][-1]+1,n+1)]
    curr = temp
curr

curr = [i+[j] for i in curr for j in range(i[-1]+1,n+1)]

n=20
k=16
def dfs(curr, other):
    if len(curr) == k:
        output.append(curr)
        return

    for i in range(len(other)):
        dfs(curr + [other[i]], other[i + 1:])


nums = list(range(1, n + 1))
output = []
dfs([], nums)
print(output)


# ----------------------

n=20
k=16
nums = list(range(1, n + 1))
output = []
queue = [([], nums)]

while queue:
    curr = queue.pop(0)
    if len(curr[0]) == k:
        output.append(curr[0])
    if len(curr[0]) > k:
        break

    for i in range(len(curr[1])):
        queue.append((curr[0] + [curr[1][i]], curr[1][i + 1:]))

print(output)

# ------------------------------


n=4
k=2
nums = list(range(1, n + 1))
start = 0
output = []
queue = [([], start)]
len_nums = len(nums)

while queue:
    curr = queue.pop(0)
    if len(curr[0])==k:
        output.append(curr[0])

    for i in range(curr[1], len_nums):
        queue.append((curr[0] + [nums[i]], i+1))

print(output)