import functools
from functools import reduce
from itertools import combinations, permutations, combinations_with_replacement


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def permutations2(candidates, k):
    res = []

    # candidates.sort()

    def dfs(curr, k):
        if len(curr) == k:
            res.append(curr[:])
            return

        # memo = set()
        for i in range(0, len(candidates)):
            # if candidates[i] in memo:
            #     continue
            # memo.add(candidates[i])
            curr.append(candidates[i])
            dfs(curr, k)
            curr.pop()

    dfs([], k)

    return res


if __name__ == '__main__':
    lis = list(range(9))
    list(filter(lambda x: x % 2 == 0, lis))

    list(map(lambda x: x % 2 == 0, lis))

    s1 = reduce(lambda x, y: x + y, lis)
    a = 6
    x = """print('a')"""
    b = eval("3+4")
    c = eval("a=5")
    d = """fdasf""dfd"""

    lis = [" ", "+", "-"]
    list(combinations(lis, 6))
    list(combinations_with_replacement(lis, 6))
    permutations2(lis, 6)
    list(permutations(lis * 6, 6))

    res = [[i] for i in lis]
    for _ in range(5):
        res = [r + [i] for r in res for i in lis]
