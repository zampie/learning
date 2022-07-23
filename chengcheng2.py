def fun(nums):
    for i in range(3, 1, -1):
        print(i)

    res = -1

    return res


if __name__ == '__main__':
    _ = input()
    nums = list(map(int, input().split()))
    res = fun(nums)
    print(res)

    # nums = [3, 3, 8, 8]
    # fun(nums)
