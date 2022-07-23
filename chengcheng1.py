def fun(x, m):
    res = 0
    for i in range(x, x + m + 1):
        s = str(i)
        s = s[::-1]

        for j in s:
            if j == '9':
                res += 1
            else:
                break

    return res


if __name__ == '__main__':
    # x, m = list(map(int, input().split()))
    x, m = 9995, 6
    res = fun(x, m)
    print(res)

    # nums = [3, 3, 8, 8]
    # fun(nums)
