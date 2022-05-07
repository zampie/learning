# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

# 暴力法 n3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxres = 0
        maxs = ''

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                temp = s[i:j]
                if temp == temp[::-1] and (j - i) > maxres:
                    maxres = j - i
                    maxs = temp

        return maxs

# 中心扩展算法 n2
s = "babad"
# s='bb'
s = "abcda"
max_len = 0
max_str = ''
for i in range(len(s)):

    # 指针中心，偶数
    j = 0
    while s[i - j] == s[i + j -1]:

        if 2 * j > max_len:
            max_len = 2 * j
            max_str = s[i - j:i + j]

        j += 1

        if i - j < 0 or i + j -1>= len(s):
            break

    # 字符中心，奇数
    j = 0
    while s[i - j] == s[i + j]:

        if (2 * j + 1) > max_len:
            max_len = 2 * j + 1
            max_str = s[i - j:i + j + 1]

        j += 1

        if i - j < 0 or i + j >= len(s):
            break
