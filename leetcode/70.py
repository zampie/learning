def climbStairs(n):
    count = 0
    if n == 1:
        print('1>')
        return 1
    if n == 2:
        print('1>1>')
        print('2>')
        return 2
    if n >= 3:
        # x = 0
        # x += climbStairs(1) * climbStairs(n - 1)
        # x += climbStairs(2) * climbStairs(n - 2)
        # return x
        return climbStairs(n - 1) + climbStairs(n - 2)


climbStairs(3)
climbStairs(4)
climbStairs(5)
climbStairs(6)

n = 5
ls = [1, 2]
for i in range(2, n):
    ls.append(ls[i - 2] + ls[i - 1])

a = 1
b = 2
n = 5
for i in range(n - 2):
    a, b = b, a + b

print(b)

a = None

if a:
    print(True)
else:
    print(False)