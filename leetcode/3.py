'''

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        x = 1
        for i in range(len(s)):
            for j in range(1, len(s) - i + 1):
                if len(s[i:i + j]) == len(set(s[i:i + j])):
                    x = max(x, j)

        return x

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res, i=0,0

        for j in range(len(s)):
            if s[j] in dic:
                i = max(i,dic[s[j]]+1)
            dic[s[j]]=j
            res = max(res, j-i+1)

        return res





'''

s = "abcabcbb"
# s = 'au'
x = 1

for i in range(len(s)):
    for j in range(1, len(s) - i+1):
        if len(s[i:i+j]) == len(set(s[i:i+j])):
            x = max(x, j)

print(x)

