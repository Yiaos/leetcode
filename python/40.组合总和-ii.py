#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(target, begin, path, ans):
            if target == 0:
                ans.append(path)
                return
            if target < 0:
                return
            for i in range(begin, len(candidates)):
                if i > begin and candidates[i] == candidates[i-1]:
                    continue
                backtrack(target-candidates[i], i+1, path+[candidates[i]], ans)

        candidates.sort()
        ans = []
        path = []
        backtrack(target, 0, path, ans)
        return ans

s=Solution()
print(s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))

# @lc code=end

