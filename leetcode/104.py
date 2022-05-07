'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node=root):
            if node:
                depth[0] += 1
                max_depth[0] = max(max_depth[0], depth[0])
                dfs(node.left)
                dfs(node.right)
                depth[0] -= 1

        depth = [0]
        max_depth = [0]
        dfs()
        return max_depth[0]





class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1





'''