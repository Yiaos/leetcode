#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left(lst, x):
            l, r = 0, len(lst) - 1
            while l <= r:
                mid = (l+r) // 2
                if x > lst[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def binary_search_right(lst, x):
            l, r = 0, len(lst) - 1
            while l <= r:
                mid = (l+r) // 2
                if x < lst[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return r
            
        left, right = binary_search_left(nums, target), binary_search_right(nums, target)
        return [left, right] if left <= right else [-1, -1]
s=Solution()
print(s.searchRange(nums = [6], target = 6))
# @lc code=end

