'''

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dic = {'1':'!@#','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        if len(digits) == 0:
            return []

        oris = []

        for s in digits:
            oris.append(dic[s])

        res = [s0 for s0 in oris[0]]
        for i in range(1, len(digits)):
            res = [s0+s1 for s0 in res for s1 in oris[i]]

        return res

'''

digits = '234'

dic = {'1':'!@#','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

if len(digits) == 0:
    print('')

oris = []

for s in digits:
    oris.append(dic[s])

res = [s0 for s0 in oris[0]]
for i in range(1, len(digits)):
    res = [s0+s1 for s0 in res for s1 in oris[i]]



# res = []
#
# for s in oris[0]:
#     res.append(s)
#
# for s0 in res:
#     for s1 in
#
# for i in range(len(oris)-1):
#     for s0 in oris[i]:
#         for s1 in oris[i+1]:
#             res.append(s0+s1)
#
