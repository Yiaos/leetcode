#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 递归， a+bc
        # ans = []
        # if len(nums) <= 1:
        #     return [nums]
        # for i in range(len(nums)):
        #     for j in self.permute(nums[:i]+nums[i+1:]):
        #         ans.append([nums[i]] + j)
        # return ans

        # 回溯
        def backtrack(nums, path, ans):
            if len(nums) == 0:
                ans.append(path)
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]], ans)
            
        ans = []
        path = []
        backtrack(nums, path, ans)
        return ans

s=Solution()
print(s.permute([1,2,3]))
        
# @lc code=end

