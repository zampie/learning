def can_construct_24pointer(nums):
    res = False

    def dfs(curr, val, text):
        nonlocal res
        if not curr:
            if abs(val - 24) < 1e-5:
                res = True
                print(text + "24")
            return

        for i in range(len(curr)):
            tmp = curr[:i] + curr[i + 1:]

            dfs(tmp, val + curr[i], f"{text} {val} + {curr[i]} = ")

            dfs(tmp, curr[i] - val, f"{text} {curr[i]} - {val} = ")
            dfs(tmp, val - curr[i], f"{text} {val} - {curr[i]} = ")

            dfs(tmp, val * curr[i], f"{text} {val} * {curr[i]} = ")

            if val != 0:
                dfs(tmp, curr[i] / val, f"{text} {curr[i]} / {val} = ")

            if curr[i] != 0:
                dfs(tmp, val / curr[i], f"{text} {val} / {curr[i]} = ")

    dfs(nums[1:], nums[0], "")
    dfs(nums[:1] + nums[2:], nums[1], "")
    dfs(nums[:2] + nums[3:], nums[2], "")
    dfs(nums[:3], nums[3], "")
    # dfs(nums, 0, "")

    print('yes' if res else 'no')


if __name__ == '__main__':
    # turn = int(input())
    # for _ in range(turn):
    #     nums = list(map(int, input().split()))
    #     can_construct_24pointer(nums)

    nums = [37, 22, 1, 1]
    can_construct_24pointer(nums)
