#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for num in nums_set:
            # 如果num-1在set中则跳过
            if num - 1 not in nums_set:
                curr_num = num
                curr_length = 1
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_length += 1
                longest = max(curr_length, longest)
        return longest
# @lc code=end

