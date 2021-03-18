#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, width = 0, len(height) -1, len(height) - 1
        ans = 0
        for w in range(width, 0, -1):
            if height[left]< height[right]:
                ans = max(w*height[left], ans)
                left += 1
            else:
                ans = max(w*height[right], ans)
                right -= 1
        return ans
# @lc code=end

