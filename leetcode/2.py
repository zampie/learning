#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        n1 = ''
        p1 = l1
        while p1 is not None:
            n1 += str(p1.val)
            p1 = p1.next
        n1 = n1[::-1]

        n2 = ''
        p2 = l2
        while p2 is not None:
            n2 += str(p2.val)
            p2 = p2.next
        n2 = n2[::-1]

        nr = str(int(n1) + int(n2))[::-1]
        print(nr)

        res = ListNode(int(nr[0]))
        pr = res
        for i in range(1, len(nr)):
            pr.next = ListNode(int(nr[i]))
            pr = pr.next

        return res
