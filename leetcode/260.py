nums = [1,2,1,3,2,5]
temp = nums[0]
for i in range(1, len(nums)):
    temp = temp ^ nums[i]

temp = 0


nums = [1,2,1,3,2,5]

a = 0
b = 0
temp = 0

for i in nums:
    temp ^= i

mask = -temp&temp


for i in nums:
    if i & mask:
        a ^=i
    else:
        b ^=i

