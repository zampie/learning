'''
        if not head:
            return head

        node1 = head
        node2 = head.next

        while node1 != None:
            while node2 != None and node1.val == node2.val:
                node2 = node2.next
            node1.next = node2
            node1 = node1.next
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        node = head

        while node!=None and node.next != None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head

'''