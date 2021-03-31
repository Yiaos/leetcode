#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i][j] = dp[i-i][j] + dp[i][j-1]
        # m = len(obstacleGrid)
        # if not m:
        #     return 0
        # n = len(obstacleGrid[0])
        # if not n:
        #     return 0
        # dp = [[0] * n for _ in range(m)]
        # # 为了防止[[1,0]]这种情况，需要先处理i==0 or j == 0的情况
        # for i in range(m):
        #     if obstacleGrid[i][0] == 0:
        #         dp[i][0] = 1
        #     else:
        #         break
        # for j in range(n):
        #     if obstacleGrid[0][j] == 0:
        #         dp[0][j] = 1
        #     else:
        #         break
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if obstacleGrid[i][j] == 1:
        #             continue
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[m-1][n-1]

        # 动态规划, faster
        # m = len(obstacleGrid)
        # if not m:
        #     return 0
        # n = len(obstacleGrid[0])
        # if not n:
        #     return 0
        # dp = [[0]*n for _ in range(m)]
        # dp[0][0] = 1 - obstacleGrid[0][0]
        # for i in range(1, m):
        #     dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
        # for j in range(1, n):
        #     dp[0][j] = dp[0][j-1] * (1 - obstacleGrid[0][j])
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1 - obstacleGrid[i][j])
        # return dp[-1][-1]

        # O(n) space
        m = len(obstacleGrid)
        if not m:
            return 0
        n = len(obstacleGrid[0])
        if not n:
            return 0       
        cur = [0]*n
        cur[0] = 1 - obstacleGrid[0][0]
        for i in range(1, n):
            cur[i] = cur[i-1] * (1-obstacleGrid[0][i])
        for i in range(1, m):
            cur[0] *= (1-obstacleGrid[i][0])
            for j in range(1, n):
                cur[j] = (cur[j-1] + cur[j]) * (1-obstacleGrid[i][j])
        return cur[-1]

        # # in place
        # if not obstacleGrid:
        #     return 
        # r, c = len(obstacleGrid), len(obstacleGrid[0])
        # obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        # for i in xrange(1, r):
        #     obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
        # for i in xrange(1, c):
        #     obstacleGrid[0][i] = obstacleGrid[0][i-1] * (1 - obstacleGrid[0][i])
        # for i in xrange(1, r):
        #     for j in xrange(1, c):
        #         obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])
        # return obstacleGrid[-1][-1]
s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]))
# @lc code=end

