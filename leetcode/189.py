nums = [1,2,3,4,5,6,7]
nums = [1,2]

k = 3

# 左移
# -------------------
for i in range(k):
    temp = nums[0]
    for i in range(1,len(nums)):

        nums[i-1] = nums[i]
    nums[-1] = temp

# 右移，向右看，需要保存当前和之前两个temp
# --------------------
temp_pre = nums[-1]
for i in range(len(nums)):
    temp_curr = nums[i]
    nums[i] = temp_pre
    temp_pre = temp_curr

# 向左看
# -------------
temp = nums[-1]
for i in range(len(nums)-1,0,-1):
      nums[i] = nums [i-1]

# 鸡贼
# -------------
nums = [1,2,3,4,5,6,7]

nums.insert(0,nums.pop())


# K跳
# -------------
for i in range(0,len(nums)):
    i = i*k%len(nums)
    print(i)
    temp_curr = nums[i]
    nums[i] = temp_pre
    temp_pre = temp_curr
