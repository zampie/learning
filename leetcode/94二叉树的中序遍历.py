'''

[1,2,3,4,5,null,null,null,6]
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        output = []
        stack =[]
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            output.append(node.val)
            node = node.right

        return output
        
'''