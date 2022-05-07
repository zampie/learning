class Solution:
    def findNumberIn2DArray(self, matrix: list, target: int) -> bool:
        if not matrix:
            return False

        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m - 1

        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False


    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in s:
            if i == ' ':
                res += '%20'
            else:
                res += i

        return res

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1

        for i in range(n - 1):
            a, b = b, a+b

        return b % 1000000007


    def hammingWeight(self, n: int) -> int:
        res = 0

        while n != 0:
            n = n & (n-1)
            res += 1

        return res

    def getKthFromEnd0(self, head, k: int):
        memo = []
        node = head

        while node:
            memo.append(node)
            node = node.next

        return memo[-k]

    def getKthFromEnd(self, head, k: int):
        former, latter = head, head

        for _ in range(k):
            former = former.next

        while former:
            former, latter = former.next, latter.next

        return latter


    def reverseList(self, head):
        if not head:
            return None

        pre = None
        node = head

        while node.next:
            temp = node.next
            node.next = pre
            pre,node = node, temp

        node.next = pre
        return node

    def mergeTwoLists(self, l1, l2):
        preNode = ListNode(-1)

        node = preNode
        p1 = l1
        p2 = l2

        while p1 and p2:
            if p1.val < p2.val:
                node.next = p1
                p1 = p1.next
            else:
                node.next = p2
                p2 = p2.next
            node = node.next

        if not p1:
            node.next = p2
        else:
            node.next = p1

        return preNode.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        return nums[size//2]



    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        memo = set()
        pA = headA
        pB = headB
        while pA:
            memo.add(pA)
            pA = pA.next
        while pB:
            if pB in memo:
                return pB
            pB = pB.next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        memo = set()
        pA = headA
        pB = headB
        while pA:
            memo.add(pA)
            pA = pA.next
        while pB:
            if pB in memo:
                return pB
            pB = pB.next



n=3
res = [1 for i in range(n,6*n+1)]
size = len(res)
p = 6**n

for sta in range(size-5):
    for i in range(sta,sta + 6):
        res[i] += 1

print(res)

for i in range(size):
    res[i] /= p

nums = [1,1,2]
target = 1

left, right = 0, len(nums) - 1
counter = 0

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        while mid > 0 and nums[mid - 1] == target:
            mid -= 1
        break
    if nums[mid] > target:
        right = mid - 1
    else:
        left = mid + 1


    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i: i+k]))

        return res


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        import collections

        queue = collections.deque([nums[0]])

        for i in range(1, k):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])

        res = [queue[0]]

        for i in range(1, len(nums) - k + 1):
            if nums[i - 1] == queue[0]:
                queue.popleft()
            while queue and nums[i + k - 1] > queue[-1]:
                queue.pop()

            queue.append(nums[i + k - 1])
            res.append(queue[0])

        return res

n = 5
m = 3
nums = list(range(n))
size = len(nums)
i = m-1

while size > 1:
    i = i % size
    nums.pop(i)
    size -= 1
    i += m-1


    print(nums)

import sys
sys.setrecursionlimit()