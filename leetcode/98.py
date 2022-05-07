'''


my
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node=root,min_limit=float('-inf'),max_limit=float('inf')):
            if not node:
                return True

            if node.left and (node.left.val >= node.val or node.left.val <= min_limit):
                return False

            if node.right and (node.right.val <= node.val or node.right.val >= max_limit):
                return False

            return helper(node.left,min_limit,node.val) and helper(node.right,node.val,max_limit)

        return helper()







# 优化，官方递归
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node=root,min_limit=float('-inf'),max_limit=float('inf')):
            if not node:
                return True

            if node.val >= max_limit or node.val <= min_limit:
                return False

            return helper(node.left,min_limit,node.val) and helper(node.right,node.val,max_limit)

        return helper()







'''