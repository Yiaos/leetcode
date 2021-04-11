#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0:
            l, r = 0, j
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                l += 1
        else:
            k = i - 1
            while k < j and nums[k] >= nums[j]:
                j -= 1
            nums[k], nums[j] = nums[j], nums[k]
            l, r = i, len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return nums

s=Solution()
print(s.nextPermutation([1,5,1]))
# @lc code=end

