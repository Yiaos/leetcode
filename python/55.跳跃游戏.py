#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心
        n = len(nums)
        step = 0
        for i in range(n):
            if i <= step:
                step = max(step, i + nums[i])
                if step >= n-1:
                    return True
        return False

s=Solution()
print(s.canJump([3,2,1,0,4]))
# @lc code=end

