#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分查找
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     mid = (l+r)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return l

        # 存在重复元素时
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) //2 
            if nums[mid] == target and nums[mid-1] != target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
s=Solution()
print(s.searchInsert([1,3,5,6],5))
# @lc code=end

