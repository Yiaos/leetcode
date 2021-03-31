#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. 动态规划
        # if n <= 2:
        #     return n
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] =  dp[i-1] + dp[i-2]
        # return dp[n]

        # 2. 动态规划
        if n <= 2:
            return n
        x = 1
        y = 2
        for i in range(3, n+1):
            x, y = y, x+y
        return y


s=Solution()
print(s.climbStairs(4))
# @lc code=end

