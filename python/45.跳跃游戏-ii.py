#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        step, max_pos, end = 0, 0, 0
        for i in range(len(nums)-1):
            if i <= max_pos:
                # 能达到的最大位置
                max_pos = max(max_pos, i+nums[i])
                # 到达边界
                if i == end:
                    step += 1
                    end = max_pos
        return step

s=Solution()
print(s.jump([2,3,1,1,4]))
# @lc code=end

