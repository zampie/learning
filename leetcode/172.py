n = 30
nums = [i for i in range(1,n+1)]


r = 1
for i in nums:
    r = i * r
    print(r)


print(r)



m2 = 0
m5 = 0
for i in range(1,n+1):
    if i%2 == 0:
        m2 +=1
    if i%5 ==0:
        m5 +=1


zeros = 0
i = 1
while 1:
    cur = n // 5**i
    if cur == 0:
        break
    zeros += cur
    i += 1

print(zeros)