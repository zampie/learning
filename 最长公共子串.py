def max_sub_string(str1, str2):
    dp = [[0] * (len(str2)) for _ in range(len(str1))]

    p = 0
    max_len = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = max(max_len, dp[i][j])
                    p = i + 1
        print(i)
        print(dp[i])

    print(max_len)
    print(p)
    return str1[p - max_len: p]


if __name__ == '__main__':
    # str1 = "1AB2345CD"
    str1 = "12345CD"
    str2 = "12345EF"

    # str1 = "abc"
    # str2 = "bcd"

    res = max_sub_string(str1, str2)
    print(res)