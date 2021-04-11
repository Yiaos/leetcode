#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(logn) ~ O(n)
        l, r = 0, len(nums) - 1
        ans = nums[0]
        while l <= r:
            mid = (l+r)//2
            # 有序, 最小值为nums[l]
            if nums[l] < nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            elif nums[l] == nums[mid]:
                ans = min(ans, nums[l])
                l = l + 1
            else:
                r = mid
        return ans
# @lc code=end

