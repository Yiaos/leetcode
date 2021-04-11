#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, ans):
            if not nums:
                ans.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]], ans)
        
        ans = []
        path = []
        nums.sort()
        backtrack(nums, path, ans)
        return ans
s=Solution()
print(s.permuteUnique([1,1,2]))
# @lc code=end

