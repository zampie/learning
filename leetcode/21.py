# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         ls = []
#         node = l1
#
#         if not l1 and not l2:
#             return None
#
#         while l1:
#             ls.append(node.val)
#             if node.next:
#                 node = node.next
#             else:
#                 break
#
#         node = l2
#         while l2:
#             ls.append(node.val)
#             if node.next:
#                 node = node.next
#             else:
#                 break
#
#         ls.sort()
#
#         res = ListNode(ls[0])
#         print(res)
#         node = res
#         print(node)
#
#         for n in ls[1:]:
#             node.next = ListNode(n)
#             node = node.next
#
#         return res


