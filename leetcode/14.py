strs = ["flower","flow","flight"]

for i in range(len(strs[0])):
    for strx in strs[1:]:
        if i < len(strx) or strx[i] != strs[0][i]:
            break



# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-prefix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ''
#
#         for i in range(len(strs[0])):
#            for strx in strs[1:]:
#                if i >= len(strx) or strx[i] != strs[0][i]:
#                     return strs[0][:i]
#
#         return strs[0]
