#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 动态规划
        m = len(grid)
        n = len(grid[0])
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = grid[0][0]
        # for i in range(1, m):
        #     dp[i][0] = dp[i-1][0] + grid[i][0]
        # for i in range(1, n):
        #     dp[0][i] = dp[0][i-1] + grid[0][i]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # return dp[-1][-1]

        # in space
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
        

s=Solution()
print(s.minPathSum([[1,2],[5,6],[1,1]]))
# @lc code=end

