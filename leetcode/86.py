'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        prehead = ListNode(0)
        prehead.next = head

        node = prehead
        while node:

            pre, p = node, node.next


            while p and p.val >= x:
                pre, p = p, p.next


            if p:
                # pre.next, node.next, p.next=p.next, p, node.next
                pre.next = p.next
                temp = node.next
                node.next = p
                p.next = temp

            node = node.next

        return prehead.next




class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        prehead = ListNode(0)
        prehead.next = head

        node = prehead

        pre, p = node, node.next

        while p:

            if p.val < x:

                # pre.next, node.next, p.next=p.next, p, node.next
                pre.next = p.next
                temp = node.next
                node.next = p
                p.next = temp
                node = node.next
                p = pre

            pre, p = p, p.next


        return prehead.next




        while node:


            while p and p.val >= x:
                pre, p = p, p.next

            if p:

                #p与node.next交换
                pre.next = p.next
                temp = node.next
                node.next = p
                p.next = temp
                # 当pre==node, node.next==p,自交换

                if node != pre:
                    p=pre.next
                else:
                    pre = p
                    p=p.next


            node = node.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        prehead = ListNode(0)
        prehead.next = head

        node = prehead

        pre, p = node, node.next

        while p:

            if p.val >= x:
                pre, p = p, p.next
            else:

                #p与node.next交换
                pre.next = p.next
                temp = node.next
                node.next = p
                p.next = temp
                # 当pre==node, node.next==p,自交换

                if node != pre:
                    p=pre.next
                else:
                    pre = p
                    p=p.next

                node = node.next

        return prehead.next

'''