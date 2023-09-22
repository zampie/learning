# 暴搜, 超时
def longestCommonSubsequence_1(text1: str, text2: str) -> int:
    res = 0

    def dfs(text1, text2, start, curr):
        nonlocal res
        res = max(res, curr)

        for i in range(start, len(text2)):
            p1 = text1.find(text2[i])
            if p1 != -1:
                dfs(text1[p1 + 1:], text2, i + 1, curr + 1)

    dfs(text1, text2, 0, 0)

    return res



def longestCommonSubsequence(text1: str, text2: str) -> int:

    dp = [[0] * (len(text2)+1) for _ in range(len(text1) + 1)]

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        print(dp[i])

    return dp[-1][-1]



if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    # text1 = "abcba"
    # text2 = "abcbcba"
    res = longestCommonSubsequence(text1, text2)
    print(res)