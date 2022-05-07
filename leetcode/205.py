st = 'egg'
res = []
memo = {}
counter = 0
for i in st:
    if i not in memo:
        memo[i] = counter
        counter += 1
    res.append(memo[i])
res


'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def trans(st):
            memo = {}
            counter = 0
            res = []
            for i in st:
                if i not in memo:
                    memo[i] = counter
                    counter += 1
                res.append(memo[i])
            
            return res
        
        return trans(s) == trans(t)

'''
for i in st:
    if i not in memo:
        memo[i] = counter
        counter += 1
    res.append(memo[i])

res.append(memo[i])
