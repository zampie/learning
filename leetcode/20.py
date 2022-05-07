'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

鸡贼
-------------------------------
class Solution:
    def isValid(self, s: str) -> bool:

        for i in range(len(s)//2):
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')

        return s==''


栈
------------------------------
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        stack = []

        for i in s:
            if i in dic:
                if stack and stack[-1] == dic[i]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(i)

        return not stack
'''

s = "()[]{}"
s = "(]"
for i in range(len(s) // 2):
    s = s.replace('()', '')
    s = s.replace('[]', '')
    s = s.replace('{}', '')

print(s == '')
