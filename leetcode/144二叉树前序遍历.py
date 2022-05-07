'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        def helper(node):
            if node != None:
                res.append(node.val)
                helper(node.left)
                helper(node.right)


        res = []
        helper(root)

        return res



# DFS
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        stack = []
        node = root

        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
                # print(node)
            node = stack.pop().right

        return res

# DFS
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        stack = [root]

        while root and stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res



'''




while 1:
    print('haha')