'''
# DFS
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        def dfs(curr=[],others=nums):
            if len(curr) == len(nums):
                output.append(curr)

            for i in range(len(others)):
                if i >0 and others[i] == others[i-1]:
                    continue
                dfs(curr+[others[i]],others[:i]+others[i+1:])


        output = []
        nums.sort()
        dfs()
        return output

# BFS
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        output = []
        nums.sort()
        queue = [([],nums)]

        while queue:
            curr = queue.pop(0)
            if len(curr[0])==len(nums):
                output.append(curr[0])
            for i in range(len(curr[1])):
                if i>0 and curr[1][i] == curr[1][i-1]:
                    continue
                queue.append((curr[0]+[curr[1][i]],curr[1][:i]+curr[1][i+1:]))


        return output
'''