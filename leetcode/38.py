'''
循环
------------------------------------------------------------
class Solution:
    def countAndSay(self, n: int) -> str:

        o_str = '1'

        if n == 1:
            return o_str

        new_str = ''
        nn = 1

        for j in range(n-1):
            for i in range(len(o_str)):
                if i+1 == len(o_str) or o_str[i] != o_str[i + 1]:
                    new_str += str(nn) + o_str[i]
                    nn = 1
                else:
                    nn += 1
            o_str = new_str
            new_str = ''

        return o_str

递归
-----------------------------------------------------------------
class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return '1'

        pre_str = self.countAndSay(n-1)

        nn = 1
        new_str = ''
        for i in range(len(pre_str)):
            if i+1 == len(pre_str) or pre_str[i] != pre_str[i + 1]:
                new_str += str(nn) + pre_str[i]
                nn = 1
            else:
                nn += 1

        return new_str


'''

n = 8
o_str = '1'

new_str = ''
nn = 1

if n == 1:
    print(o_str)

for j in range(n-1):
    for i in range(len(o_str)):
        if i+1 == len(o_str) or o_str[i] != o_str[i + 1]:
            new_str += str(nn) + o_str[i]
            nn = 1
        else:
            nn += 1
    o_str = new_str
    new_str = ''

print(o_str)
























