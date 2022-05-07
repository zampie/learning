'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join([str(i) for i in digits])
        res = str(int(s)+1)
        return [int(i) for i in res]

'''


digits = [1,2,3]
s = ''
for d in digits:
    s = s+str(d)

num = str(int(s)+1)

output = []

for n in num:
    output.append(int(n))

print(output)