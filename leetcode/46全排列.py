'''
# DFS
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        def dfs(curr=[],other=nums):
            if len(curr) == len(nums):
                output.append(curr)
            for i in range(len(other)):
                dfs(curr+[other[i]],other[:i]+other[i+1:])

        output = []
        dfs()
        return output


# BFS
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        array = [([],nums)]
        output = []

        while array:
            curr = array.pop(0)
            if len(curr[0]) == len(nums):
                output.append(curr[0])
            for i in range(len(curr[1])):
                array.append((curr[0]+[curr[1][i]],curr[1][:i]+curr[1][i+1:]))


        return output

'''



nums = [1,2,3]

array = [([],nums)]
output = []

while array:
    curr = array.pop(0)
    if len(curr[0]) == len(nums):
        output.append(curr[0])
    for i in range(len(curr[1])):
        array.append((curr[0]+[curr[1][i]],curr[1][:i]+curr[1][i+1:]))

print(output)

# -----------------------------------

nums = [1,2,3]

stack = []
output = []
curr = ([],nums)
i = 0

for i in range(len(nums)):
    while curr[1]:
        stack.append(curr)
        curr = (curr[0]+[curr[1][i]],curr[1][:i]+curr[1][i+1:])
        output.append(curr[0])
curr = stack.pop()
i += 1


# -----------------------------
def dfs(curr=[], other=nums):
    if len(curr) == len(nums):
        output.append(curr)
    for i in range(len(other)):
        dfs(curr + [other[i]], other[:i] + other[i + 1:])


output = []
dfs()

