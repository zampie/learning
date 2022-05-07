'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def dfs(node=root):
            if node!=None:
                curr[0] += node.val
                # print(curr[0])
                # print(curr[0] == sum)
                if not node.left and not node.right and curr[0] == sum:
                    flag[0] = True
                dfs(node.left)
                dfs(node.right)
                curr[0] -= node.val


        curr = [0]
        flag = [False]
        dfs()

        return flag[0]




'''