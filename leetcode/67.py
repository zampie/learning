nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1 = nums1[:m]
nums1.extend(nums2[:n])
nums1.sort()
