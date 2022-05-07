'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append([node, False])
                node = node.left

            while stack:
                if stack[-1][1]:
                    output.append(stack.pop()[0].val)
                else:
                    break

            if stack:
                stack[-1][1] = True
                node = stack[-1][0].right

        return output



class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            #  如果stack[-1]还有右子树
            if stack[-1].right:
                # 把stack[-1]的右子树作为空处理（改变原树，不安全），更新node
                stack[-1].right, node= None, stack[-1].right
            # 如果stack[-1]没有右子树，弹出
            else:
                output.append(stack.pop().val)
                # 弹出栈尾,下次循环时再更新node

        return output

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append([node, False])
                node = node.left

            if stack[-1][1] == True or not stack[-1][0].right:
                output.append(stack.pop()[0].val)
            else:
                stack[-1][1] = True
                node = stack[-1][0].right

        return output


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append([node, False])
                node = node.left

            if stack[-1][1] == True:
                output.append(stack.pop()[0].val)
            else:
                stack[-1][1] = True
                node = stack[-1][0].right


        return output
'''