
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# my
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = [[]]
        depthes = [0]
        queue = [root]

        while queue:
            node = queue.pop(0)
            depth = depthes.pop(0)
            if len(res) == depth:
                res.append([node.val])
            else:
                res[depth].append(node.val)
            if node.left:
                queue.append(node.left)
                depthes.append(depth+1)
            if node.right:
                queue.append(node.right)
                depthes.append(depth+1)

        return res


# 官方
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        depth = 0
        queue = deque([root])

        while queue:
            res.append([])

            for i in range(len(queue)):
                node = queue.popleft()
                res[depth].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth +=1

        return res


# DFS

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        def dfs(node=root,depth=0):
            if node:
                if len(res) == depth:
                    res.append([node.val])
                else:
                    res[depth].append(node.val)

                dfs(node.left, depth+1)
                dfs(node.right, depth+1)

        res = []
        dfs()

        return res

'''




import math

temp = [3,9,20,None,None,15,7,None,None,None,None]
res = [[] for _ in range(math.ceil(math.log2(len(temp) + 1)))]
for i in range(len(temp)):
    if temp[i] != None:
        res[int(math.log2(i + 1))].append(temp[i])

if not res[-1]:
    res.pop()


from collections import deque


import math
math.factorial(10)

from functools import reduce

reduce(lambda a,b:a+b,[3,4,5,6,6,6],5)