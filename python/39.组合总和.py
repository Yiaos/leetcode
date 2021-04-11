#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(target, begin, path, ans):
            if target == 0:
                ans.append(path)
                return
            # 剪枝， 终止回溯
            if target < 0:
                return
            for i in range(begin, len(candidates)):
                backtrack(target-candidates[i], i, path+[candidates[i]], ans)
        ans = []
        path = []
        candidates.sort()
        backtrack(target, 0, path, ans)
        return ans

s=Solution()
print(s.combinationSum(candidates = [2,3,5], target = 8))
# @lc code=end

