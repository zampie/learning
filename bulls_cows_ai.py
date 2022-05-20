def permute():
    res = []

    def dfs(candidates, curr):
        if len(curr) == 4:
            res.append(curr[:])
            return

        for i in range(len(candidates)):
            dfs(candidates[:i] + candidates[i + 1:], curr + [candidates[i]])

    nums = list(range(0, 10))
    dfs(nums, [])

    return res


if __name__ == '__main__':
    res = permute()
    print(res)
    print(len(res))
