height = [1,8,6,2,5,4,8,3,7]













class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_w = 0

        for i in range(len(height)):
            for j in range(i+1,len(height)):
                w = min(height[i],height[j]) * (j-i)
                max_w = max(max_w, w)

        return max_w