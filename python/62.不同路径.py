#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. 动态规划
        if not m or not n:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for j in range(n):
            for i in range(m):
                if j == 0 or i == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

        # 2.排列组合
        # 从左上角到右下角共需移动m+n-2次，其中m-1次向下移动， n-1次向右移动
        # 路径总数即为 从m+n-2次移动中选择m-1次向下移动的方案数
        # 即：C(m+n-2, n-1)
        # import math
        # if not m or not n:
        #     return 0
        # return math.factorial(m+n-2)/(math.factorial(n-1) * math.factorial(m-1))

        # 3. O(n) space
        # if not n or not n:
        #     return 0
        # cur = [1] * n
        # for i in range(1, m):
        #     for j in range(1, n):
        #         cur[j] += cur[j-1]
        # return cur[-1]


s=Solution()
print(s.uniquePaths(1,2))
# @lc code=end

