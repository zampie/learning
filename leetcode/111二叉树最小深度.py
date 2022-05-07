'''
# DFS0
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # if not root.left and not root.right:
        #     return 1

        depth_left = self.minDepth(root.left)
        depth_right = self.minDepth(root.right)
        if not root.left:
            return depth_right + 1
        if not root.right:
            return depth_left + 1

        return min(depth_left,depth_right) + 1



# DFS1
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node=root,depth=0):
            if node:
                if not node.left and not node.right:
                    min_depth[0] = min(min_depth[0], depth+1)

                dfs(node.left,depth+1)
                dfs(node.right,depth+1)

        min_depth = [float('inf')]
        dfs()
        return min_depth[0]



'''