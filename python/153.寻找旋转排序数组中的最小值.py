#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = nums[0]
        while l <= r:
            mid = (l+r)//2
            # 有序, 最小值为nums[l]
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            else:
                r = mid
        return ans
s=Solution()
print(s.findMin([3,4,5,1,2]))
# @lc code=end

