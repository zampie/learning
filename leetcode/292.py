'''

你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。

你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。

示例:

输入: 4
输出: false
解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
     因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。


# 贼
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 != 0



# 递归，超出递归深度
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <=3:
            return True

        return not(self.canWinNim(n-3) and self.canWinNim(n-2) and self.canWinNim(n-1))



# 循环版动态规划，超内存
class Solution:
    def canWinNim(self, n: int) -> bool:
        d = [True] * n
        for i in range(3, len(d)):
            d[i] = not(d[i-3] and d[i-2] and d[i-1])

        return d[-1]

# 动态规划优化内存，超时
class Solution:
    def canWinNim(self, n: int) -> bool:
        d0, d1, d2, d3 = True, True, True, True
        for i in range(n-3):
            d3 = not(d0 and d1 and d2)
            d0, d1, d2 = d1, d2, d3

        return d3




'''


def canWinNim(n: int):
    if n <= 3:
        return True

    return not (canWinNim(n - 3) and canWinNim(n - 2) and canWinNim(n - 1))

canWinNim(20)


def canWinNim(n):
    d0, d1, d2, d3 = True, True, True, True
    for i in range(n - 3):
        d3 = not (d0 and d1 and d2)
        d0, d1, d2 = d1, d2, d3

    return d3

canWinNim(1348820612)

