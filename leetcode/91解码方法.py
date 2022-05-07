'''




# Error,递归
class Solution:
    def numDecodings(self, s: str) -> int:

        if len(s)==1:
            return 1
        if len(s)==2:
            return 1 if int(s)>26  else 2

        if int(s[-2:])>26:
            return self.numDecodings(s[:-1])
        else:
            return self.numDecodings(s[:-1]) + self.numDecodings(s[:-2])



# 循环DP，一万种特殊情况
class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0]=='0':
            return 0
        if len(s)==1:
            return 1

        dp = [0] * len(s)
        dp[0] = 1 if s!=0 else 0

        temp = s[:2]
        if temp =='10' or temp =='20' or (temp >'26'and temp[-1]!='0'):
            dp[1]=1
        elif temp>'10' and temp <='26':
            dp[1]=2
        else:
            dp[1]=0

        print(dp)
        for i in range(2,len(s)):
            if s[i] !='0':
                dp[i] += dp[i-1]


            if s[i-1:i+1]>='10' and s[i-1:i+1]<='26':
                dp[i] += dp[i-2]





        return dp[-1]





'''

s='0'



d1 = 1
d2 = 1 if int(s) > 26 else 2

while len(s) > 0:
    if int(s[-2:]) > 26:
        d3 = d2
    else:
        d3 = d1 + d2
    s = s[:-2]
    d1, d2 = d2, d3