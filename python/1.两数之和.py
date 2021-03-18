#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: nums[int]
        :type target: int
        :rtype: nums[int]
        """
        hashmap=dict()
        for i, num in enumerate(nums):
            remain = target - num
            if remain in hashmap:
                return [hashmap[remain], i]
            hashmap[num] = i
    

# @lc code=end

